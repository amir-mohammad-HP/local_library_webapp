from sre_parse import CATEGORIES
from django.views.generic import ListView
from books.models import Book, BookCopy
from search.forms import SearchForm
from itertools import chain
from datetime import date

# Create your views here.
class Search(ListView):
    model = Book
    paginate_by = 20
    template_name = 'search/results.html'
    copy = True

    def get_queryset(self, *args, **kwargs):

        form = SearchForm(self.request.GET)

        if not form.is_valid():
            return form
        model = form.cleaned_data['model']

        if not (len(form.cleaned_data['isbn']) == 0):
            query = BookCopy.objects.filter(isbn = form.cleaned_data['isbn'])
            return query

        if model == 'books':
            query = self.model_book(form)
            
        elif model == 'copies':
            query = self.model_copy(form)

        else:
            return self.model.objects.none()
        
        return query
    

    def get_context_data(self, **kwargs) :
        ctx = super().get_context_data(**kwargs)
        ctx['copy'] = self.copy
        form = SearchForm(self.request.GET)
        ctx['form'] = form
        return ctx


    def Q_category_none_all(self, query, obj, obj_name_filter):

        if obj is not None:
            if obj != 'all':
                query = query.filter(**{f'{obj_name_filter}' : obj})
                return query
        
        return  query

    def Q_category_none(self, query, obj, obj_name_filter):

        if obj is not None:
            query = query.filter(**{f'{obj_name_filter}' : obj})
            return query
        
        return  query

    def Q_category_empty(self, query, obj, obj_name_filter):
        if obj != '':
            query = query.filter(**{f'{obj_name_filter}' : obj})
            return query
        
        return query.none()


    def model_book(self, form):
        self.copy = False

        query = Book.objects.all()
        
        published = form.cleaned_data['published_date']
        if published is not None:
            by_date = self.Q_category_none(BookCopy.objects.all(), published.year, 'published_on__year')
            query = query.filter(id__contains=by_date.values_list('book'))

        q_title = self.Q_category_empty(BookCopy.objects.all(), form.cleaned_data['title'], 'book__title__contains')

        q_author = self.Q_category_empty(BookCopy.objects.all(), form.cleaned_data['author_translator'], 'author__contains')

        q_translator = self.Q_category_empty(BookCopy.objects.all(), form.cleaned_data['author_translator'], 'translator__contains')

        copy_query = q_title.union(q_author, q_translator)

        query = query.filter(id__contains=copy_query.values_list('book'))

        query = self.Q_category_none_all(query, form.cleaned_data['category'], 'category__name')
        query = self.Q_category_none_all(query, form.cleaned_data['language'], 'language')

        query = query.order_by('-title')

        return query

    
    def model_copy(self, form):
        self.copy = True

        query = BookCopy.objects.all()

        published = form.cleaned_data['published_date']
        if published is not None:
            query = self.Q_category_none(query, published.year, 'published_on__year')

        query = self.Q_category_none_all(query, form.cleaned_data['category'], 'book__category__name')
        query = self.Q_category_none_all(query, form.cleaned_data['language'], 'book__language')

        q_title = self.Q_category_empty(query, form.cleaned_data['title'], 'book__title__contains')

        q_author = self.Q_category_empty(query, form.cleaned_data['author_translator'], 'author__contains')

        q_translator = self.Q_category_empty(query, form.cleaned_data['author_translator'], 'translator__contains')

        query = q_title.union(q_author, q_translator)
        
        query = query.order_by('-book')

    
        return query
