from django.contrib import admin
from apps.content.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'author_full_name', 'description', 'price', 'image', 'created_at', 'updated_at',]
    list_display_links = list_display

