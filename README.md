# Credit Cortex

A Django REST Framework API for managing customer and loan data, checking eligibility, and generating loan analytics.  

---

## 🚀 Features
- Customer CRUD (Create, Read, Update, Delete)
- Loan CRUD (Create, Read, Update, Delete)
- Check loan eligibility
- Swagger UI API documentation
- SQLite database (configurable to PostgreSQL/MySQL)
- RESTful API endpoints

---

## 📸 Screenshots

### 1. Home Interface
![WhatsApp Image 2025-08-14 at 18 04 23](https://github.com/user-attachments/assets/f11698f9-56c0-4eb0-a6d2-58924b906020)

### 2. Starting the Docker
![WhatsApp Image 2025-08-14 at 17 34 15](https://github.com/user-attachments/assets/6e60d6bb-97d8-4bee-a4d6-e012fd8b571a)


### 3. API - Docs
![WhatsApp Image 2025-08-14 at 17 56 44](https://github.com/user-attachments/assets/ca77360d-df13-4b7e-988e-2400a52ae22e)


### 4. Customer Loan List
![WhatsApp Image 2025-08-14 at 17 39 53](https://github.com/user-attachments/assets/0ca0a3ee-0c94-4051-af84-151fa96c9580)


### 5. Customer  List
![WhatsApp Image 2025-08-14 at 17 41 27](https://github.com/user-attachments/assets/3f262a08-28f9-4d52-848d-e6b40591e635)


### 6. Customer  Instance
![WhatsApp Image 2025-08-14 at 17 43 14](https://github.com/user-attachments/assets/64a4358b-a5c3-4922-8c89-4ce4b0856723)


### 7. Delete Customer Instance
![WhatsApp Image 2025-08-14 at 17 50 46](https://github.com/user-attachments/assets/7f7bd2b6-3c70-4b49-8449-a1b68da88d92)


### 8. Create Loan
![WhatsApp Image 2025-08-14 at 17 36 36](https://github.com/user-attachments/assets/a55fcb7d-0b60-4594-aa86-7265ab10a02b)


### 9. Loan List
![WhatsApp Image 2025-08-14 at 17 51 15](https://github.com/user-attachments/assets/53cd4e15-7b96-4a0c-9776-6932f2abd9c3)


### 10. Loan Instance
![WhatsApp Image 2025-08-14 at 17 51 38](https://github.com/user-attachments/assets/4a7cb67e-0d14-4662-9d2c-47d0b81a31b9)


### 11. Loan Check Elgliblty 
![WhatsApp Image 2025-08-14 at 18 11 51](https://github.com/user-attachments/assets/3a4766a7-9a83-4282-b32d-337236c5cb10)


---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/your-username/credit-cortex.git
cd credit-cortex

# Create virtual environment
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```
## 🔗 API Endpoints

### Customers
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/customers/` | List all customers |
| POST   | `/api/customers/` | Create a customer |
| GET    | `/api/customers/{id}/` | Retrieve a customer |
| PUT    | `/api/customers/{id}/` | Update a customer |
| DELETE | `/api/customers/{id}/` | Delete a customer |
| GET    | `/api/customers/{id}/loans/` | Get customer loans |

### Loans
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/loans/` | List all loans |
| POST   | `/api/loans/` | Create a loan |
| GET    | `/api/loans/{id}/` | Retrieve a loan |
| PUT    | `/api/loans/{id}/` | Update a loan |
| DELETE | `/api/loans/{id}/` | Delete a loan |

### Additional
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/api/check-eligibility/` | Check loan eligibility |

---

## 📄 Example Request (Eligibility)

**Request:**
```json
POST /api/check-eligibility/
{
    "customer_id": 1,
    "loan_amount": 500000,
    "interest_rate": 12,
    "tenure": 24
}

```
**Response:**
```json
{
    "eligible": false,
    "reason": "EMI exceeds approved limit"
}
```
## 🛠 Tech Stack
- Python 3.x
- Django
- Django REST Framework
- SQLite
- Swagger UI

---

📧 **Contact:** [princebaghal637@gmail.com](mailto:princebaghal637@gmail.com)



