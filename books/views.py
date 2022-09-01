from books.models import Book, BookCopy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.forms import models as model_forms
from library.help_classes import common_template
from books.forms import BookCopyForm, BookForm
from django.utils.translation import gettext_lazy as _
# Create your views here.
class AllBooks(common_template, ListView):
    model = Book
    template_name = 'books/AllBooks.html'
    view = 'all'

class Create(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/create.html'
    success_url = reverse_lazy('books:all_books')

    def form_valid(self, form) :
        obj = form.save(commit=False)
        obj.save()
        print(obj.id)
        self.get_success_url(pk = obj.pk)
        return super().form_valid(form)

    def get_success_url(self, **kwargs) -> str:
        if kwargs:
            self.success_url = reverse_lazy('books:book', kwargs = {'pk':kwargs['pk']}) 
        return self.success_url

class Edit(UpdateView):
    queryset = Book.objects.all()
    form_class = BookForm
    template_name = 'books/create.html'
    # success_url = reverse_lazy('books:all_books')

    def get_success_url(self) -> str:
        self.success_url = reverse_lazy('books:book', kwargs = {'pk':self.kwargs['pk']}) 

class Del(DeleteView):
    model = Book
    template_name = 'books/delete.html'
    success_url = reverse_lazy('books:all_books')

class theBook(ListView):
    model = BookCopy
    template_name = 'books/book.html'
    context_object_name = 'copies'

    def get_queryset(self):
        return super().get_queryset().filter(book__id = self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['book'] = Book.objects.get(id = self.kwargs.get('pk'))
        return ctx


class craeteCopy(CreateView):
    model = BookCopy
    template_name = 'books/create.html'
    form_class = BookCopyForm
    
    def get_success_url(self) -> str:
        return reverse_lazy('books:book', kwargs = {'pk':self.kwargs['pk']})
    
    def form_valid(self, form):
        
        object = form.save(commit =False)
        object.book = Book.objects.get(id = self.kwargs['pk'])
        object.save()
        
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['book'] = Book.objects.get(id = self.kwargs['pk'])
        return ctx

class Del_copy(DeleteView):
    model = BookCopy
    template_name = 'books/delete_copy.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('books:book', kwargs = {'pk':self.kwargs['p2k']})

class Edit_copy(UpdateView):
    model = BookCopy
    form_class = BookCopyForm
    template_name = 'books/create.html'
    # success_url = reverse_lazy('books:all_books')

    def get_success_url(self) -> str:
        return reverse_lazy('books:book', kwargs = {'pk':self.kwargs['p2k']})
