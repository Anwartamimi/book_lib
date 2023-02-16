from django.views.generic import ListView, DetailView
from .models import Book, Category
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import BookRentHistory, InboxMessage
from .forms import ContactForm
from django.http import Http404, HttpResponseForbidden



class HomeListView(ListView):
    model = Book
    template_name='books/home.html'

    def get_queryset(self):
        queryset = super(HomeListView, self).get_queryset()
        return queryset.all().order_by('-id')[:5]
        


class BooksListView(ListView):
    model = Book
    template_name = 'books/books.html'
    
    def get_queryset(self):
        return Book.objects.order_by('-id')[:10]


class SearchBookListView(ListView):
    model = Book
    template_name = 'books/book_search_result.html'

    def get_queryset(self):
        queryset = super(SearchBookListView, self).get_queryset()
        q = self.request.GET.get('q')
        if q:
           books_by_title = queryset.filter(title__icontains=q)
           books_by_author = queryset.filter(author__icontains=q)
           return books_by_title | books_by_author
        return queryset


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    
    def get_success_url(self):
        return reverse('bookDetail', kwargs={'slug': self.object.slug})


class CategoryBookListView(ListView):
    model = Category
    template_name = 'books/books_by_category.html'

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['slug'])
        return Book.objects.filter(category=category)


@login_required(login_url='login')
def confirm_rent_view(request, slug):
    try:
        b = Book.objects.get(slug=slug)
        if b.book_amount <= 0:
            messages.warning(
                request, f'You cant rent this book')
            return redirect('bookDetail', slug=b.slug)
    except Book.DoesNotExist:
        raise Http404("We dont have this book")
    return render(request, 'books/confirm_rent_view.html', {'book': b})


@login_required(login_url='login')
def rent_book_view(request, slug):
    try:
        b = Book.objects.get(slug=slug)
        if b:
            if b.book_amount > 0:
                b.book_amount -= 1
                b.save()
                log_history = BookRentHistory(user=request.user, book=b)
                log_history.save()
                messages.success(
                    request, f'You rent a book: {b.title}')
            else:
                messages.warning(
                    request, f'You cant rent this book')
                return redirect('bookDetail', slug=b.slug)
    except Book.DoesNotExist:
        raise Http404("Book is unavailable")
    return redirect('UserProfile')


@login_required(login_url='login')
def return_book_view(request, slug):
    try:
        b = Book.objects.filter(slug=slug)[0]
        if b:
            b.book_amount += 1
            b.save()
            log_history = BookRentHistory.objects.filter(book=b)[0]
            log_history.delete()
            messages.success(
                request, f'You successfully returned a book: {b.title}')
        else:
            messages.warning(
                request, f'Error occurs, sorry')
            return redirect('UserProfile')
    except Book.DoesNotExist:
        raise Http404("Book is unavailable now ")
    return redirect('UserProfile')


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            new_message = InboxMessage()
            new_message.name = name
            new_message.email = email
            new_message.message = message
            new_message.save()
            messages.success(request, f'Your message sent successfully')            
            return redirect('home')

    if request.user.is_authenticated:
        form = ContactForm()
        form.fields['name'].initial = request.user.username
        form.fields['email'].initial = request.user.email
        form.fields['message'].widget.attrs['placeholder']='Write your message..'
        form.fields['name'].widget.attrs['readonly'] = True
        form.fields['email'].widget.attrs['readonly'] = True
        form.fields['name'].label = 'Login'
        return render(request, 'books/contact.html', {'form': form})
    else:
        form = ContactForm()
        form.fields['name'].widget.attrs['placeholder'] = 'Your name'
        form.fields['email'].widget.attrs['placeholder'] = 'Your email'
        form.fields['message'].widget.attrs['placeholder'] = 'Write your message here'
        return render(request, 'books/contact.html', {'form': form})
