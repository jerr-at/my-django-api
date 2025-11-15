**beKind – UPI Donation Platform (Django)**
A simple and elegant Django-based donation platform where users can contribute funds via UPI and instantly appear on a Live Donor Wall.
This project focuses on clean UI, secure form handling, and real-time data display — ideal for beginners learning Django.

** Features**
1.UPI-based donation flow
2. Secure donor form (name, email, amount, message)
3. Live Donor Wall showing all contributors
4. Donor details stored securely in the database
5. Django Admin Panel for donor management
6. Clean, responsive UI using Django templates

**Tech Stack**
**Backend:** Django (Python)
**Frontend:** HTML, CSS, Bootstrap
**Database: **SQLite
**Forms:** Django ModelForms
**Admin: **Django Admin

**Project Structure**
donation_site/
│── donation/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│── donation_site/
│   ├── urls.py
│── templates/
│   ├── home.html
│   ├── donors.html
│── manage.py

**Donor Model**
class Donor(models.Model):
    name        # Donor's name
    email       # Email address
    amount      # Donation amount (₹)
    message     # Optional message
    donated_at  # Timestamp

**Getting Started:**
1. Clone the repository
git clone https://github.com/jerr-at/your-repo-name.git
cd your-repo-name
2. Install dependencies
pip install -r requirements.txt
3. Apply migrations
python manage.py migrate
4. Start server
python manage.py runserver
Open:
 http://127.0.0.1:8000/

**🔗 How the Donation Flow Works:**

1.User opens the homepage
2.Fills the donation form
3.Completes payment via UPI
4.Submits the form with details
5.Data is saved securely via ModelForm
6.Donor appears instantly on the Live Donor Wall

**Django Admin Access:**
Create an admin account:
python manage.py createsuperuser
Use Django Admin to view, edit, or delete donation entries.

**What I Learned:**
1.Django models, forms, views
2.Secure user input handling
3.Saving and displaying real-time database data
4.Using Django templates for UI
5.Managing entries through Django Admin
This project helped me combine backend logic with frontend presentation while learning core Django workflows.

**Future Enhancements:**
Real-time UPI payment verification
Donor leaderboard
Email/receipt notifications
Pagination and search for donor list

**License:**
MIT License.
