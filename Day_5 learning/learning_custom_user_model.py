
# Create a Custom User Model

# By default, Django provides a User model with these fields:
# username, first_name, last_name, email, password, etc.
# But in real-world apps, we often want to:
# Use email instead of username for login
# Add custom fields like phone number, birthdate, etc.
# Have complete control over authentication and user creation


# To do this, Django lets us override the default user model using:
# AbstractBaseUser
# AbstractUser


# 2. AbstractBaseUser vs AbstractUser

# Feature             	        AbstractUser	                    AbstractBaseUser

# Inherits default User fields	Yes (username, first name, etc.)	No
# Flexibility	                    Medium	                            High (create from scratch)
# Recommended for	                Modifying existing User fields	    Completely custom User model
# Needs custom UserManager?	    Optional	                        Required


# AbstractUser

# Pre-built user model with common fields.
# You can extend it to add fields like phone number.

# from django.contrib.auth.models import AbstractUser

# class MyUser(AbstractUser):
#     phone_number = models.CharField(max_length=10)



# AbstractBaseUser

# Only gives 
# password & last_login
# need to define your own fields (like email, name, etc.)
# Gives full control over authentication.

# BaseUserManager

# Django uses a manager to create and manage users in the database.
# When we use AbstractBaseUser, we must define a custom manager using BaseUserManager because the default manager expects username.

# Custom Manager 

# from django.contrib.auth.models import BaseUserManager

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Email is required')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)

# Full Custom User Model (Using AbstractBaseUser)

# models.py

# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Users must have an email address')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=100)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']  # Needed for superuser creation


# Settings Configuration

# In settings.py, tell Django to use your custom user model:

# AUTH_USER_MODEL = 'app_name.CustomUser'
