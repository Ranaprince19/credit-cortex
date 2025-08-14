from django.urls import path, include
from .views import CheckEligibilityView
from rest_framework.routers import DefaultRouter
from .views import (
    CustomerViewSet,
    LoanViewSet,
    CustomerLoansView,
    LoanAnalyticsView,
    RegisterCustomerView,
    CheckEligibilityView,
    CreateLoanView,
    ViewLoanDetailView,
    ViewCustomerLoansWithEmi,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = "loan_api"

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'loans', LoanViewSet, basename='loan')

schema_view = get_schema_view(
   openapi.Info(
      title="Loan API",
      default_version='v1',
      description="API documentation for the Loan Approval System",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # ---- Custom endpoints FIRST to avoid router conflicts ----
    path('customers/<int:customer_id>/loans/', CustomerLoansView.as_view(), name='customers_loans_list'),
    path('customers/<int:customer_id>/loans-with-emi/', ViewCustomerLoansWithEmi.as_view(), name='loans_with_emi'),
    path('loans/analytics/', LoanAnalyticsView.as_view(), name='loans_analytics'),
    path('register/', RegisterCustomerView.as_view(), name='register_customer'),
    path('check-eligibility/', CheckEligibilityView.as_view(), name='check_eligibility'),
    path('create-loan/', CreateLoanView.as_view(), name='create_loan'),
    path('loan/<int:loan_id>/', ViewLoanDetailView.as_view(), name='view_loan_detail'),


    # ---- Router AFTER custom endpoints ----
    path('', include(router.urls)),

    # ---- Docs ----
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
