ATM Management System – Full Documentation

## 📌 Project Overview
ATM Management System is a full-stack, backend-focused web application that simulates real ATM functionalities.  
The system is built using Django and follows secure coding practices for authentication and transaction management.

---

## 🚀 Features
- User Authentication (Card Number & PIN)
- Secure Session Handling
- Deposit & Withdraw Money
- Balance Enquiry (PIN-protected)
- Fund Transfer Between Accounts
- Mini Statement (Transaction History)
- Change PIN Functionality
- Error Handling & Input Validation

---

## Tech Stack
- Backend: Python, Django
- Frontend: HTML, CSS
- Database: SQLite (default) / MySQL
- Version Control: Git & GitHub

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
git clone https://github.com/nkadam96/ATM-Management-System.git
cd ATM-Management-System
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Apply Migrations
python manage.py migrate
5️⃣ Run Development Server
python manage.py runserver
Open browser and visit:

cpp
Copy code
http://127.0.0.1:8000/

🔐 Security Highlights
    1.PIN-based authentication
    2.Session-based access control
    3.Protected routes for sensitive operations
    4.Server-side validation

📂 Project Structure

ATM-Management-System/
│── atm_project/
│── manage.py
│── requirements.txt
│── README.md
│── PROJECT_DOCUMENTATION.md
🎯 Use Case
This project is ideal for:
  1.Learning Django backend development
  2.Understanding session handling
  3.Demonstrating CRUD & transaction logic
  4.Showcasing a real-world banking simulation project

👤 Author
Nagin Kadam
Aspiring Backend / Python Developer

📌 GitHub: https://github.com/nkadam96


