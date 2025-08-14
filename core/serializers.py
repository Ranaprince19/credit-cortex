from rest_framework import serializers
from decimal import Decimal
from .models import Loan, Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"

    def validate(self, attrs):
        amt = Decimal(str(attrs.get('loan_amount', '0')))
        rate = Decimal(str(attrs.get('interest_rate', '0')))
        tenure = attrs.get('tenure') or 0

        if amt <= 0:
            raise serializers.ValidationError("loan_amount must be > 0")
        if rate < 0:
            raise serializers.ValidationError("interest_rate cannot be negative")
        if not isinstance(tenure, int) or tenure <= 0:
            raise serializers.ValidationError("tenure (months) must be a positive integer")
        
        return attrs
