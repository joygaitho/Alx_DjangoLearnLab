# Intro to Django

This repository is an introductory guide and starter project for **Django**, a high-level Python web framework designed for rapid development and clean, pragmatic design.

Django is maintained by the **Django Software Foundation** and is widely used in production web applications.  
Official documentation: https://docs.djangoproject.com/

---

## What Is Django?

Django is a **Model–View–Template (MVT)** web framework that helps developers build secure, maintainable web applications efficiently.

Key characteristics (from official documentation):
- Written in **Python**
- Follows the **DRY (Don’t Repeat Yourself)** principle
- Includes built-in tools for authentication, admin panels, ORM, and routing

Source:  
https://docs.djangoproject.com/en/stable/intro/overview/

---

## Prerequisites

Before starting, make sure you have:

- **Python 3.10+**  
  Verify installation:
  ```bash
  python --version

Installation

Create and activate a virtual environment (recommended)

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

Install Django

pip install django

Verify installation:

django-admin --version

Creating a Django Project

Create a new project:

django-admin startproject myproject
cd myproject


Project structure (officially documented):

manage.py – command-line utility

myproject/ – project configuration

settings.py

urls.py

asgi.py

wsgi.py

Source:
https://docs.djangoproject.com/en/stable/intro/tutorial01/

Running the Development Server

Start the local development server:

python manage.py runserver


Then open your browser at:

http://127.0.0.1:8000/


Source:
https://docs.djangoproject.com/en/stable/intro/tutorial01/#the-development-server

Creating an App

In Django, projects are made up of apps.

Create an app:

python manage.py startapp myapp


Apps are reusable components that handle specific functionality.

Source:
https://docs.djangoproject.com/en/stable/intro/tutorial01/#creating-the-polls-app

Django Admin

Django includes a built-in admin interface.

To enable it:

python manage.py createsuperuser


Then log in at:

http://127.0.0.1:8000/admin/


Source:
https://docs.djangoproject.com/en/stable/intro/tutorial02/

Learning Goals

This repository is intended to help beginners understand:

Django project vs app structure

URL routing

Views and templates

Models and the ORM

Admin interface

Development server workflow

Official Learning Resources

All recommended resources are maintained by the Django project:

Django Documentation:
https://docs.djangoproject.com/

Django Tutorial (Beginner):
https://docs.djangoproject.com/en/stable/intro/tutorial01/

Django GitHub Repository:
https://github.com/django/django