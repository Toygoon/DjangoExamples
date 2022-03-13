from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from books.models import Book, Author, Publisher

# Create your views here.

# TemplateView
class BooksModelView(TemplateView):
    template_name = 'books/index.html'
    
    def get_context_data(self, **kwargs):
        # Super method must be called for the first line in get_context_data
        context = super().get_context_data(**kwargs)
        # To show the list to the first screen in books application
        context['model_list'] = ['Book', 'Author', 'Publisher']
        
        return context
    
# ListView
class BookList(ListView):
    # Import all records from the book, and construct it into object_list
    model = Book
    
class AuthorList(ListView):
    model = Author
    
class PublisherList(ListView):
    model = Publisher
    
# DetailView
class BookDetail(DetailView):
    model = Book
    
class AuthorDetail(DetailView):
    model = Author
    
class PublisherDetail(DetailView):
    model = Publisher