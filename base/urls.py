from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('author/<str:pk>/', views.author, name='author'),
    path('book/<str:pk>/', views.book, name='book'),
    path('book_form', views.book_form, name='book_form'),
    path('update_author/<str:pk>/', views.update_author, name='update_author'),
    path('all_books', views.all_books, name='all_books'),
    path('all_authors', views.all_authors, name='all_authors'),
]