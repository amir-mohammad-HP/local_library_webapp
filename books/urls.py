from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('', views.AllBooks.as_view(), name = 'all_books'),
    path('create/', views.Create.as_view(), name= 'create'),
    path('edit/<pk>/', views.Edit.as_view(), name= 'edit'),
    path('delete/<pk>/', views.Del.as_view(), name= 'delete'),
    path('<pk>/', views.theBook.as_view(), name = 'book'),
    # path('search/', views.Search.as_view(), name = 'search'),
    path('<pk>/create/', views.craeteCopy.as_view(), name = 'create_copy'),
    path('<p2k>/edit/<pk>/', views.Edit_copy.as_view(), name= 'edit_copy'),
    path('<p2k>/delete/<pk>/', views.Del_copy.as_view(), name= 'delete_copy'),
]
