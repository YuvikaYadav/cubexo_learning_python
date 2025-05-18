# forms are used to collect user input. Django provides a powerful and secure way to work with forms using its built-in forms module. This allows developers to:

# Define input fields
# Perform validation
# Automatically generate HTML inputs
# Handle secure submission (CSRF protection)


# Why Use ?
# Less manual coding of form elements in HTML
# Clean and validated data from cleaned_data
# Reusable and maintainable code
# Strong security with CSRF tokens

# # forms.py
# from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, label="Your Name")
#     email = forms.EmailField(label="Your Email")
#     message = forms.CharField(widget=forms.Textarea, label="Your Message")


# CharField – Single-line text input
# EmailField – Validates email format
# Textarea – Multi-line input using widget=forms.Textarea


# Rendering Form in Template (HTML)

# <form method="POST">
#   {% csrf_token %}
#   {{ form.as_p }} <!-- Auto renders with <p> tags -->
#   <button type="submit">Send</button>
# </form>

# Manual Rendering

# <form method="POST">
#   {% csrf_token %}
#   {{ form.name.label_tag }} {{ form.name }}
#   {{ form.email.label_tag }} {{ form.email }}
#   {{ form.message.label_tag }} {{ form.message }}
#   <button type="submit">Submit</button>
# </form>


# # views.py
# from django.shortcuts import render
# from .forms import ContactForm

# def contact_view(request):
#     form = ContactForm()
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Use cleaned_data to access the validated data
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             # You can now save, send email, or process data
#     return render(request, "contact.html", {"form": form})

# Form Input Types
# Django Field	   Input Type	    Description

# CharField	         text	        Single-line text
# EmailField	         email	        Input for emails
# IntegerField         number	        Input for numbers
# BooleanField         checkbox	    True/False
# ChoiceField	         select	        Dropdown
# DateField	         date	        Date picker
# FileField	         file	        Upload file
# ImageField	         file	        Upload image only


# Form Methods

# is_valid() – Checks if all inputs are valid
# cleaned_data – Access to validated input values
# form.errors – View validation errors

# Custom Validation 

# class ContactForm(forms.Form):
#     email = forms.EmailField()

#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if not email.endswith("@gmail.com"):
#             raise forms.ValidationError("Only Gmail addresses allowed")
#         return email


# A ModelForm connects a Django model with a form, allowing auto-generation of form fields based on the model.

# Use
# Avoid writing repetitive form fields
# Automatically handle saving to the database
# Easy form + model integration


# Basic Example:

# # models.py
# from django.db import models

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     age = models.IntegerField()

# # forms.py
# from django.forms import ModelForm
# from .models import Student

# class StudentForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = ['name', 'email', 'age']

# Using ModelForm in View

# # views.py
# from .forms import StudentForm

# def student_view(request):
#     form = StudentForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     return render(request, 'student_form.html', {'form': form})

# Customizing Widgets and Labels

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['name', 'email', 'age']
#         labels = {
#             'name': 'Full Name',
#             'email': 'Email Address',
#         }
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
#             'age': forms.NumberInput(attrs={'class': 'form-control'}),
#         }

# Custom Validation 

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = '_all_'

#     def clean_age(self):
#         age = self.cleaned_data.get('age')
#         if age < 18:
#             raise forms.ValidationError("Age must be 18 or above")
#         return age

# Saving Without Committing

# if form.is_valid():
#     student = form.save(commit=False)
#     student.age += 1  # modify before saving
#     student.save()

# Django shell commands are command-line utilities that allow developers to interact with their Django projects. They can execute database queries, manage migrations, create superusers, and perform various administrative tasks.


 










