from django.contrib import admin

# Register your models here.
from .models import Comment

#allow the admin to modify the Comment tables in the database
admin.site.register(Comment)