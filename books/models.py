from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime
from django.utils.text import slugify

class Category(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.category

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super(Category, self).save(*args, **kwargs)

    
class Book(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=1000, default='About book')
    image = models.ImageField(
        default='default_book.png', upload_to='books_pics')
    author = models.CharField(max_length=100)
    book_amount = models.IntegerField()
    publish_date = models.DateField()
    number_of_pages = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)
    
class BookRentHistory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, editable=False)
    rent_date = models.DateField(auto_now_add=True, editable=False)
    back_date = models.DateField(default=datetime.now()+timedelta(days=30))

    def __str__(self):
        return f'{self.book.title}'
        
    @property
    def how_many_days(self):
        return (self.back_date - datetime.now().date())[:2]

   
    
     

class InboxMessage(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return f'Message from {self.name}'