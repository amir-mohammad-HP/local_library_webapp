from books.models import Category, Book
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from library.help_classes import common_template

from books.forms import CategoryForm

# Create your views here.
class AllCategories(ListView):
    models = Category
    queryset = Category.objects.all()
    template_name = 'theCategories/AllCategories.html'

class Create(CreateView):
    form_class = CategoryForm 
    queryset = Category.objects.all()
    template_name = 'theCategories/create.html'
    success_url = reverse_lazy('theCategories:all_categories')

class Edit(UpdateView):
    queryset = Category.objects.all()
    form_class = CategoryForm 
    template_name = 'theCategories/create.html'

    def get_success_url(self) -> str:
        return reverse_lazy('theCategories:the_category', kwargs = {'pk':self.kwargs['pk']})

class Del(DeleteView):
    model = Category
    template_name = 'theCategories/delete.html'
    success_url = reverse_lazy('theCategories:all_categories')

class theCategories(common_template, ListView):
    model = Book
    template_name = 'books/AllBooks.html'
    view = 'category'

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().filter(category__id = self.kwargs['pk'])

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['category'] = Category.objects.get(id = self.kwargs['pk'])
        return ctx
    
    