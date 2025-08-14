import pandas as pd
from core.models import Customer, Loan

def run():
    customer_df = pd.read_excel('D:/Downloads2/trial11/customer_data.xlsx')
    loan_df = pd.read_excel('D:/Downloads2/trial11/loan_data.xlsx')

    # Strip columns
    customer_df.columns = customer_df.columns.str.strip()
    loan_df.columns = loan_df.columns.str.strip()

    print("🧾 Columns in customer_data.xlsx:", customer_df.columns.tolist())
    print("🧾 Columns in loan_data.xlsx:", loan_df.columns.tolist())

    # Load customer data
    for _, row in customer_df.iterrows():
        Customer.objects.update_or_create(  # safe insert
            customer_id=row['Customer ID'],
            defaults={
                "name": row['First Name'] + " " + row['Last Name'],
                "email": f"{row['First Name'].lower()}.{row['Last Name'].lower()}@example.com",
                "date_of_birth": "2000-01-01",
                "address": "Unknown",
                "phone": row['Phone Number'],
                "joined_date": "2023-01-01",
            }
        )

    # Load loan data
    for _, row in loan_df.iterrows():
        customer = Customer.objects.get(customer_id=row['Customer ID'])
        Loan.objects.update_or_create(  # safe insert
            loan_id=row['Loan ID'],
            defaults={
                "customer": customer,
                "loan_amount": row['Loan Amount'],
                "loan_type": "Personal Loan",
                "status": "approved",
                "created_date": row['Date of Approval'],
            }
        )

run()
