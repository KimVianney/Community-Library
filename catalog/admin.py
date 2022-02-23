from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

# Define the admin class
class BookInline(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    #Show which fields to display on admin site
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    # Show which fields to display in detail view, also showing how to lay them out
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

# Tabular inline view class to be displayed inside Book detail view on admin site
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # def display_genre(self):
    #     """Create a string for the genre. This is required to display the genre in Admin."""
    #     return ', '.join(genre.name for genre in self.genre.all()[:3])

    # display_genre.short_description = 'Genre'

    # list_display = ('title', 'author', 'display_genre')
    list_display = ('title', 'author')

    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )



#Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)