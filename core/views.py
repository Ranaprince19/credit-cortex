from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Loan
from .serializers import CustomerSerializer, LoanSerializer

# Full CRUD for Customer
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Full CRUD for Loan
class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

# Additional endpoints (optional)
class CustomerLoansView(APIView):
    def get(self, request, customer_id):
        loans = Loan.objects.filter(customer_id=customer_id)
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LoanAnalyticsView(APIView):
    def get(self, request):
        loans = Loan.objects.all()
        total_loans = loans.count()
        total_amount = sum(loan.loan_amount for loan in loans)
        status_counts = {
            "approved": loans.filter(status="approved").count(),
            "pending": loans.filter(status="pending").count(),
            "rejected": loans.filter(status="rejected").count()
        }

        data = {
            "total_loans": total_loans,
            "total_amount": total_amount,
            "status_counts": status_counts
        }
        return Response(data)
class RegisterCustomerView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            approved_limit = int(request.data.get('monthly_salary')) * 36
            serializer.save(approved_limit=approved_limit)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CheckEligibilityView(APIView):
    def post(self, request):
        customer_id = request.data.get('customer_id')
        loan_amount = request.data.get('loan_amount')
        interest_rate = request.data.get('interest_rate')
        tenure = request.data.get('tenure')

        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}, status=404)

        emi = (float(loan_amount) * (1 + float(interest_rate) / 100)) / int(tenure)
        if emi * tenure <= customer.approved_limit:
            return Response({"eligible": True, "approved_loan_amount": loan_amount}, status=200)
        else:
            return Response({"eligible": False, "reason": "EMI exceeds approved limit"}, status=200)
class CreateLoanView(APIView):
    def post(self, request):
        data = request.data
        customer_id = data.get('customer_id')

        # Check eligibility again
        eligibility_check = CheckEligibilityView().post(request)
        if not eligibility_check.data.get("eligible"):
            return Response({"error": "Customer not eligible"}, status=400)

        loan = Loan.objects.create(
            customer_id=customer_id,
            loan_amount=data['loan_amount'],
            interest_rate=data['interest_rate'],
            tenure=data['tenure'],
            emi=(float(data['loan_amount']) * (1 + float(data['interest_rate']) / 100)) / int(data['tenure']),
            status="approved"
        )
        return Response(LoanSerializer(loan).data, status=201)
class ViewLoanDetailView(APIView):
    def get(self, request, loan_id):
        try:
            loan = Loan.objects.get(id=loan_id)
        except Loan.DoesNotExist:
            return Response({"error": "Loan not found"}, status=404)

        loan_data = LoanSerializer(loan).data
        customer_data = CustomerSerializer(loan.customer).data
        return Response({"loan": loan_data, "customer": customer_data}, status=200)
class ViewCustomerLoansWithEmi(APIView):
    def get(self, request, customer_id):
        loans = Loan.objects.filter(customer_id=customer_id)
        loans_with_emi = [loan for loan in loans if loan.emi > 0]
        serializer = LoanSerializer(loans_with_emi, many=True)
        return Response(serializer.data, status=200)
