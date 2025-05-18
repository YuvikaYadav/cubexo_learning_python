# # Django - Intro and Features

# #Installation pip install django

# Django was invented by Lawrence Journal-World in 2003, Initial release to the public was in July 2005. 
# Latest version 5.0.4
# django-admin --version

# Django is a back-end server side web framework.
# Django is free, open source and written in Python.
# Django makes it easier to build web pages using Python

# Django emphasizes reusability of components, also referred to as DRY (Don't Repeat Yourself), and comes with ready-to-use features like login system, database connection and CRUD operations (Create Read Update Delete).

# Django is especially helpful for database driven websites.

# Features

# It provides a user authentication system that helps in managing accounts and passwords.
# Django projects can quickly switch from small-scale projects to large-scale ones.
# Django is also believed to be a versatile framework, giving developers the flexibility to build various types of applications.
# It provides a good sense of security by avoiding common threats like cross-site scripting, SQL injection, etc.
# Django is very popular amongst the web frameworks because of its vast community support that helps a developer while working.

# Cross-site scripting (XSS) is a web security vulnerability that allows an attacker to inject malicious scripts into a website, which are then executed by the victim's browser. These scripts can steal user data, hijack accounts, or redirect users to malicious sites. 

# Attackers can use SQL injection on an application if it has dynamic database queries that use string concatenation and user supplied input


# to check the commands available
# django-admin

# to create a virtaul  environment
# python -m venv Venv_name

# to activate the venv
# Venv_name\Scripts\activate

# to creare project 
# django-admin startproject project_name

# cd project_directory
# run the server
# python manage.py runserver

# to create app
# python manage.py startapp app_name