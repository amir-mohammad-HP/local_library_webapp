from email.policy import default
from django import forms 
from books import models
from django.forms.widgets import TextInput, Select, DateInput
from django.utils.translation import gettext_lazy as _

def category_sort(item):
    return (item, item)

class SearchForm(forms.Form):
    title = forms.CharField(
        label = _('Title'),
        max_length= 250,
        widget= TextInput(
            attrs={
                    'type' : "text",
                    'class' : "input-form",
                }
        ),
        required=False,
    )
    author_translator = forms.CharField(
        label = _('Author/Translator'),
        max_length= 250,
        widget= TextInput(
            attrs={
                    'type' : "text",
                    'class' : "input-form",
                }
        ),
        required=False,
    )
    language = forms.ChoiceField(
        choices = (('all', _('All')),) + models.LANGUAGES ,
        label = _('language'),
        widget = Select(
                attrs={
                    'type' : "button",
                    'class' : "input-form",
                }),
        required=False,
    )
    category = forms.ChoiceField(
        choices = (('all', _('All')),) + tuple(category_sort(item) for item in models.Category.objects.all()),
        label = _('Category'),
        widget = Select(
                attrs={
                    'type' : "button",
                    'class' : "input-form",
                }),
        required=False,
    )
    published_date = forms.DateField(
        label = _('pulished year'),
        widget = DateInput(
                attrs={
                    'type':'date',
                    'class' : "input-form ",
                }),
        required=False,
    )
    isbn= forms.CharField(
        label = _('ISBN'),
        max_length= 15,
        widget= TextInput(
            attrs={
                    'type' : "text",
                    'class' : "input-form",
                }
        ),
        required=False,
    )
    model= forms.ChoiceField(
        choices=(
            ('copies', _('copies')), 
            ('books', _('books')),
            ),
        label = _('search in '),
        widget= Select(
            attrs={
                    'type' : "text",
                    'class' : "input-form",
                }
        ),
        required=False,
    )