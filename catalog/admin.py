from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from django.db import models

# Register your models here.

from .models import Author, Genre, Book, BookInstance

# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(Book)
# admin.site.register(BookInstance)

class BookInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

admin.site.register(Book, BookAdmin)

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('Instance', {
            "fields": (
                'book', 'imprint', 'id'
            ),
        }),
        ('Availability', {
            "fields": (
                'status', 'due_back'
            )
        }),
    )

admin.site.register(BookInstance, BookInstanceAdmin)
