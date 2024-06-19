from django.urls import path
from . import views



urlpatterns = [
    path('', views.signup, name='signup'),  # Signup page
    path("login/", views.user_login , name="user_login"),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('book_list/', views.book_list, name='book_list'),  # Home page listing all books
    path('books/<int:pk>/', views.book_detail, name='book_detail'),  # Book detail page
    path('books/<int:book_id>/add_review/', views.add_review, name='add_review'),  # Add review page
    path('add_book/', views.add_book, name='add_book'),
]



