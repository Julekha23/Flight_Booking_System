# ✈️ Flight Booking System (FBS)

A web-based **Flight Booking System** developed using Python and Django. This project allows users to search for flights, create an account, log in, book flights, and manage their bookings through a simple web interface.

## 📌 Features

* **User Registration:** Create a new account with personal details.
* **User Login:** Authenticate users using Django's built-in authentication system.
* **Flight Search:** Search for available flights based on source, destination, and departure date.
* **Flight Details:** View flight information, including airline, flight number, departure, arrival, and price.
* **Flight Booking:** Book flights by providing passenger details and a seat number.
* **My Bookings:** View your flight bookings.
* **Cancel Booking:** Cancel an existing flight booking.
* **User Profile:** Access the profile page after logging in.
* **Admin Panel:** Manage application data through Django's administration interface.

## 🛠️ Technologies Used

* **Backend:** Python, Django
* **Frontend:** HTML, CSS
* **Database:** SQLite
* **Authentication:** Django Authentication System
* **Version Control:** Git and GitHub

## 📂 Project Structure

```text
FBS/
│
├── account/
│   ├── migrations/
│   ├── templates/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── profile.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── booking/
│   ├── migrations/
│   ├── templates/
│   │   ├── booking.html
│   │   └── mybook.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── flights/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── FBS/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   └── style.css
│
├── tmp/
│   ├── home.html
│   ├── main.html
│   └── nav.html
│
├── manage.py
├── db.sqlite3
└── README.md
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Julekha23/Flight_Booking_System.git
```

Navigate to the project directory:

```bash
cd FBS
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Install Django

```bash
python -m pip install django
```

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an administrator account.

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 🗄️ Database Models

### 1. Flight Model

Stores flight information, including:

* Flight number
* Airline name
* Source and destination
* Departure and arrival times
* Ticket price
* Number of seats

### 2. Booking Model

Stores booking information, including:

* User who made the booking
* Selected flight
* Passenger name
* Seat number
* Booking date

### 3. User Model

Uses Django's built-in User model to manage user accounts and authentication.

## 🚀 Application Workflow

1. A user opens the Flight Booking System.
2. The user registers for an account or logs in.
3. The user searches for flights by entering the source, destination, and departure date.
4. The user selects a flight.
5. The user enters the passenger name and seat number.
6. The system saves the booking in the database.
7. The user can view their bookings and cancel a booking.

## 🎯 Project Objectives

* Understand Django's Model-View-Template (MVT) architecture.
* Implement user registration and authentication.
* Perform database operations using Django ORM.
* Build a flight search and booking workflow.
* Understand URL routing, views, models, and templates.
* Develop a database-driven web application using Python and Django.

## 🔮 Future Enhancements

* Online payment integration.
* Automatic seat availability management.
* Email confirmation after booking.
* Flight filters and sorting.
* Booking history and downloadable tickets.
* Improved form validation and error handling.
* Responsive user interface for mobile devices.

## 👩‍💻 Author

**Julekha Molla**

---

⭐ If you find this project useful, consider giving the repository a star!
