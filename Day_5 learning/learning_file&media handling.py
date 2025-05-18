# File uploads (like images, documents, PDFs, etc.) are handled via:

# Model Fields: FileField / ImageField
# Forms: ModelForm or Form
# Media Files: Files that users upload (not static files like CSS/JS)


# FileField and ImageField

# FileField:

# Used for any file (PDF, doc, zip, etc.)
# file = models.FileField(upload_to='uploads/')

# ImageField:

# Used only for images. Requires Pillow library.
# pip install Pillow
# image = models.ImageField(upload_to='images/')

# File Upload Settings in settings.py

# To handle uploaded files, you need to define media settings:

# import os

# MEDIA_URL = '/media/'  # URL to access media files
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Folder to save uploaded files


# Setting

# MEDIA_URL	What the browser will use to access files (e.g., http://localhost:8000/media/myfile.jpg)
# MEDIA_ROOT	Where the files are stored in project directory


# Example file path: project_root/media/images/myimg.jpg



# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     # your URLs
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.db import models

# class Document(models.Model):
#     title = models.CharField(max_length=100)
#     upload = models.FileField(upload_to='docs/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

# This will store files in:

# /media/docs/filename.pdf


# from django import forms
# from .models import Document

# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ['title', 'upload']


# views.py:

# from django.shortcuts import render
# from .forms import DocumentForm

# def upload_file(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return render(request, 'success.html')
#     else:
#         form = DocumentForm()
#     return render(request, 'upload.html', {'form': form})

# Always use request.FILES to handle uploaded files.


# upload.html:

# <form method="POST" enctype="multipart/form-data">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <button type="submit">Upload</button>
# </form>

# enctype="multipart/form-data" is required for file uploads.


# {% for doc in documents %}
#     <p>{{ doc.title }}</p>
#     <a href="{{ doc.upload.url }}">Download</a>
# {% endfor %}


# {{ file_field.url }}

# file.url gives the complete URL path starting with /media/...


# Validation
# Limit file size:
# def validate_file_size(value):
#     limit = 2 * 1024 * 1024  # 2 MB
#     if value.size > limit:
#         raise ValidationError('File too large. Size should not exceed 2 MB.')

# upload = models.FileField(upload_to='docs/', validators=[validate_file_size])


