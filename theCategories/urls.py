from django.urls import path
from theCategories import views

app_name = 'theCategories'

urlpatterns = [
    path('', views.AllCategories.as_view(), name = 'all_categories'),
    path('create/', views.Create.as_view(), name= 'create'),
    path('<pk>/edit/', views.Edit.as_view(), name= 'edit'),
    path('<pk>/delete/', views.Del.as_view(), name= 'delete'),
    path('<pk>/', views.theCategories.as_view(), name = 'the_category'),

]
