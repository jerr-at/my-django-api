



beKind – UPI Donation Platform 

Project Overview:
This is a simple and user-friendly donation platform built using Django. Users can donate money through UPI and have their details displayed on a live donor wall. The focus of the project is to learn Django fundamentals such as models, forms, views, templates, and admin functionality.
Features:
1. Users can donate any amount via UPI.
2. Secure donor form collects name, email, amount, and an optional message.
3. Donor details are stored in the database.
4. Live Donor Wall displays all contributions.
5. Admin panel allows complete donor management.
6. Safe handling of user input using Django ModelForms.
7. Responsive design that works on desktop and mobile.
Tech Stack:
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap
Database: SQLite
Forms: Django ModelForms
Admin: Django Admin

Project Structure:
donation_site/
- donation/
  - models.py
  - forms.py
  - views.py
  - urls.py
- donation_site/
  - urls.py
- templates/
  - home.html
  - donors.html
- manage.py
Donor Model Description:
The Donor model contains the following fields:
- name: Name of the donor
- email: Email address
- amount: Donation amount (in ₹)
- message: Optional message
- donated_at: Timestamp of the donation
Setup Instructions:
Step 1: Install dependencies:
pip install -r requirements.txt
Step 2: Apply migrations:
python manage.py migrate
Step 3: Start the development server:
python manage.py runserver
Open the application in browser at:
http://127.0.0.1:8000/

Admin Panel Access:
Create a superuser account with:
python manage.py createsuperuser
Access the admin panel at:
http://127.0.0.1:8000/admin/
How the Donation Flow Works:
1. User opens the homepage.
2. User fills the donation form.
3. User completes the UPI payment.
4. Form data is validated and saved.
5. Donor appears instantly on the donor wall.
Learning Outcomes:
- Understanding Django models, views, templates, and forms
- Handling user input securely
- Displaying dynamic data
- Using Django Admin for backend management
- Integrating backend and frontend components

Future Enhancements:
- UPI payment verification
- Leaderboard for top donors
- Email receipts for donations
- Pagination for donor list

