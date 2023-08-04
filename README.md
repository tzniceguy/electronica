# Electronica 


## Description

Electronica is an e-commerce store and a subsidiary of Swahilielite, offering the latest electronic gadgets and accessories. This repository contains the source code for the Electronica website.

## Features

- User registration and login functionality.
- Browse and search for electronic products.
- View product details and add products to the cart.
- Secure checkout and payment processing.
- Admin dashboard for managing products and orders.

## Technologies Used

- Django: A high-level Python web framework.
- Bootstrap 5: A popular CSS framework for responsive and mobile-first design.
- SQLite: A lightweight, built-in database used for development purposes.
- Other Python packages (e.g., django-allauth, django-crispy-forms, etc.).

## Installation and Setup

1. Clone the repository
   git clone https://github.com/tzniceguy/electronica.git


2. Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate

3. Install the required dependencies:
pip install -r requirements.txt


4. Run database migrations:


5. Create a superuser to access the admin dashboard:

python manage.py createsuperuser


6. Start the development server:

python manage.py runserver


7. Open your browser and navigate to http://localhost:8000/ to access the Electronica website.

## How to Contribute

Contributions are welcome! If you have any suggestions, bug reports, or new features to add, please feel free to create a pull request or open an issue.

## License

This project is licensed under the [MIT License](LICENSE).




