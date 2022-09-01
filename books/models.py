import uuid
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

# Create your models here.
LANGUAGES = (
        ('persian' , _('persian')),
        ('english' , _('english')),
        ('arabic' , _('arabic')),
        ('other' , _('other')),
    )
    
class Category(models.Model):
    name = models.CharField(
        max_length = 200, 
        unique = True, 
        null = True,
        validators=[
            MinLengthValidator(2, _('must be at least 2 characters')),
        ],)
    
    sign = models.CharField(max_length = 1, blank=True, null=True, default=None)
    num = models.IntegerField(
        validators=[
            MinValueValidator(1), MaxValueValidator(20) 
    ],
    default=None,
    blank=True,
    null = True,
    )

    create_on = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-create_on']
    

    def __str__(self) -> str:
        return self.name
        
    def get_signiture(self):
        return f'{self.sign}{self.num}'

    def get_view(self):
        return reverse('theCategories:the_category', kwargs = {'pk' : self.id})

    def get_edit_view(self):
        return reverse('theCategories:edit', kwargs = {'pk' : self.id})
    
    def get_delete_view(self):
        return reverse('theCategories:delete', kwargs = {'pk' : self.id})
    
    def get_books_number(self):
        return len(BookCopy.objects.filter(book__category__id = self.id))


class Book(models.Model):
    title = models.CharField(
        max_length=250,
         unique=True,
         validators=[
            MinLengthValidator(2, 'must be at least 2 characters'),
        ]
        )
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    create_on = models.DateTimeField(auto_now_add=True, editable=False)
    update_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category',on_delete = models.SET_NULL, null=True, blank=True,)
    language = models.CharField(max_length=10, choices = LANGUAGES, default='persian')

    class Meta:
        ordering = ['-update_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.category:
            # print(Category.objects.get(name = 'No Category'))
            self.category = Category.objects.get(name = 'No Category')

        super(Book, self).save(*args, **kwargs)

    def get_view(self):
        return reverse('books:book', kwargs = {'pk' : self.id})

    def get_edit_view(self):
        return reverse('books:edit', kwargs = {'pk' : self.id})

    def get_delete_view(self):
        return reverse('books:delete', kwargs = {'pk' : self.id})

    def get_create_copy_view(self):
        return reverse('books:create_copy', kwargs = {'pk' : self.id})

    def get_copies(self):
        return BookCopy.objects.filter(book__id = self.id)


class BookCopy(models.Model):

    book = models.ForeignKey('Book', on_delete = models.CASCADE)
    author = models.CharField(max_length=250, blank=True, null=True)
    translator = models.CharField(max_length=250, blank=True, null=True)
    published_on = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length = 15, blank=True, null = True)
    # language + ' ' + category + ' ' + book.id + ' ' + copy.id
    shelf_code = models.CharField(max_length = 50, blank=True, null=True) 

    def get_book_view(self):
        return reverse('books:book', kwargs= {'pk': self.book.id})

    def get_edit_view(self):
        return reverse('books:edit_copy', kwargs={'p2k':self.book.id, 'pk':self.id})
    
    def get_delete_view(self):
        return reverse('books:delete_copy', kwargs={'p2k':self.book.id, 'pk':self.id})


