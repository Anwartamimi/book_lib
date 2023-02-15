from django.urls import path
from .views import (
    HomeListView,
    SearchBookListView,
    BooksListView,
    BookDetailView,
    CategoryBookListView,
    confirm_rent_view,
    rent_book_view,
    return_book_view,
    )

from django.conf import settings
from django.conf.urls.static import static

from .views import contact_form

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('search-book-results', SearchBookListView.as_view(), name='search'),
    path('books/', BooksListView.as_view(), name='books'),
    path('book/<slug:slug>', BookDetailView.as_view(), name='bookDetail'),
    path('books-by-category/<slug:slug>',
         CategoryBookListView.as_view(), name='category-booklist'),
    path('confirm-rent-a-book/<slug:slug>', confirm_rent_view, name='confirm_rent_view'),
    path('book/rent_book/<slug:slug>', rent_book_view , name='rent_book') , 
    path('book/return-book/<slug:slug>', return_book_view, name='return_book'),
    path('contact', contact_form, name='contact'),  
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
