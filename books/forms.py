from django.forms import ModelForm
from books.models import Book, BookCopy, Category
from django.forms.widgets import TextInput, Select, DateInput
from django.utils.translation import gettext_lazy as _

class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name', ]
        labels = {
            'name': _('Category name'),
        }
        # help_texts = {
        #     'name': 'Some useful help text.',
        # }
        error_messages = {
            'name': {
                'max_length': _("This name is too long."),
            },
        }

        widgets = {
            'name': TextInput(
                attrs={
                    'type' : "text",
                    'class' : "input-form",
                }),
        }

class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'category', 'language', ]
        labels = {
            'title': _('Title'),
            'category' : _('Category'),
            'language' : _('Language')
        }
        # help_texts = {
        #     'name': 'Some useful help text.',
        # }
        error_messages = {
            'title': { 
                'max_length': _("This name is too long."),
            },
        }

        widgets = {
            'title': TextInput(
                attrs={
                    'type' : "text",
                    'class' : "input-form",
                }),
            'category': Select(
                attrs={
                    'type' : "button",
                    'class' : "input-form",
                }),
            'language': Select(
                attrs={
                    'type' : "button",
                    'class' : "input-form",
                }),
        }

class BookCopyForm(ModelForm):

    class Meta:
        model = BookCopy
        fields = ['author', 'translator', 'published_on', 'isbn', ]
        labels = {
            'author' :_("Author"), 
            'translator' : _("Translator"), 
            'published_on' : _("Published on"), 
            'isbn' : _("isbn".upper()),
        }

        widgets = {
            'author' :TextInput(
                attrs={
                    'type' : "text",
                    'class' : "input-form",
                }),
            'translator' : TextInput(
                attrs={
                    'type' : "text",
                    'class' : "input-form",
                }),
            'published_on' : DateInput(
                attrs={
                    'type':'date',
                    'class' : "input-form",
                }), 

            'isbn' : TextInput(
                attrs={
                    'type' : "text",
                    'class' : "input-form",
                }),
        }

        