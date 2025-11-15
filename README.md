beKind – UPI Donation Platform (Django)

A simple and user-friendly Django-based donation platform where users can contribute funds via UPI and instantly appear on a Live Donor Wall.
This project focuses on clean UI, secure form handling, and real-time data display — ideal for learning core Django concepts.

Features

UPI Donations: Users can donate any amount via UPI.

Secure Donor Form: Collects name, email, amount, and an optional message.

Live Donor Wall: Displays all contributions in real time.

Admin Panel: Full donor management using Django Admin.

Form Validation: Safe handling of user input with Django ModelForms.

Responsive Design: Works smoothly on desktop and mobile.

Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS, Bootstrap

Forms: Django ModelForms

Database: SQLite

Admin: Django Admin

Project Structure
donation_site/
│── donation/
│   ├── models.py        # Donor model
│   ├── forms.py         # Donor form
│   ├── views.py         # Logic for donation & donor wall
│   ├── urls.py          # App routing
│── donation_site/
│   ├── urls.py          # Project routing
│── templates/
│   ├── home.html        # Donation form UI
│   ├── donors.html      # Donor wall
│── manage.py

Donor Model
class Donor(models.Model):
    name        # Donor's name
    email       # Email address
    amount      # Donation amount (₹)
    message     # Optional note
    donated_at  # Timestamp of donation

Quick Start
1. Install dependencies
pip install -r requirements.txt

2. Run migrations
python manage.py migrate

3. Start server
python manage.py runserver


Open the application:

👉 http://127.0.0.1:8000/

How the Donation Flow Works

User fills the donation form

User makes payment through UPI

Form is submitted with details

Django saves data securely

Donor appears instantly on the Live Donor Wall

Admin Access

Create superuser:

python manage.py createsuperuser


Login at:

👉 http://127.0.0.1:8000/admin/

What I Learned

Django models, views, forms

Handling user input securely

Connecting backend logic with frontend templates

Using Django Admin for data management

Rendering real-time data on the UI

Future Enhancements

Real UPI payment verification

Donor leaderboard

Email receipts

Pagination for Donor Wall

License

This project is open-source under the MIT License.
