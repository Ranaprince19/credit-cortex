from django.db import models

class Customer(models.Model):
    customer_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    joined_date = models.DateField()
    approved_limit = models.IntegerField(default=0)  # ✅ Add this field


    def __str__(self):
        return self.name

class Loan(models.Model):
    loan_id = models.CharField(max_length=20, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_amount = models.FloatField()
    loan_type = models.CharField(max_length=50)
    status = models.CharField(max_length=20)  # approved, pending, rejected
    created_date = models.DateField()

    def __str__(self):
        return f"{self.loan_id} - {self.customer.name}"
