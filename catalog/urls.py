from django.template.defaulttags import url
from django.urls import path, re_path

from locallibrary import settings
from . import views
from django.views.static import serve

urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('author_list/', views.AuthorListView.as_view(), name='author_list'),
    path('author_detail/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),
    path('my_books/', views.LoanedBooksByUserListView.as_view(), name='my_books'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.author_delete, name='author_delete'),
    path('book/<uuid:pk>/loan/', views.loan_book_librarian, name='loan_book_librarian'),
    path('available/', views.AvailBooksListView.as_view(), name='all_available'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
