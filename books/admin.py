from django.contrib import admin
from books.models import Book, Category, BookCopy

# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_on', 'slug')
    # list_filter = ('')
    search_fields = ['title', 'author', 'translator']
    prepopulated_fields = {'slug' : ['title','language']}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sign', 'num')
    search_fields = ('name', )

class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('book', 'shelf_code', 'isbn')
    search_fields = ('book', 'isbn')
    list_filter = ['published_on',]


admin.site.register(Book, BooksAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BookCopy, BookCopyAdmin)
