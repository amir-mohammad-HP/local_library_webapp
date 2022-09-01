from atexit import register
from django import template
from books.models import BookCopy

register = template.Library()

def bookcopy (value, arg):
    if arg == 'number of copies':
        return len(BookCopy.objects.filter(book = value))
    return 'not found'

register.filter('bookcopy', bookcopy)

