# Coffee Shop

Welcome to the Coffee Shop project! This Django application is designed to
manage a coffee shop's products, orders, and users efficiently.

## Requirements

- **PostgreSQL** (Make sure it's installed and running)
- **Python 3.12.4**

### Installation Guide

Clone this repository

- Set your pythonr virtual enviroment
- install the dependencies `pip install -r requirements.txt`
  - (optional) you can also install the dev dependencies `pip install -r requirements-dev.txt`
- Create a `.env` file in the root of the project. You can use `.env.example`.
  - Add your database credentials and other necessary configurations to `.env`.
- Create the PostgreSQL database and apply migrations.

  ```bash
  psql -U postgres CREATE DATABASE coffeeshop;
  ```

- Apply migrations

  ```bash
  python manage.py migrate
  ```

- Create a Superuser to access the Django admin interface.

  ```python
  python manage.py createsuperuser
  ```

- Start the Django development server.

  ```bash
  ./manage.py runserver
  ```

Access the project by navigating to `http://127.0.0.1:8000` in your web browser.

## Project Structure

- **products**: Handles everything related to coffee products.
- **users**: Manages user authentication and profiles.
- **orders**: Manages customer orders.
