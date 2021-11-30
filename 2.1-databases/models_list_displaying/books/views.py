from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, template, context)


def books_by_date(request, pub_date):
    template = 'books/books_by_date.html'
    books = Book.objects.filter(pub_date=pub_date)
    next_date = str(Book.objects.order_by('-pub_date').filter(pub_date__gt=pub_date).values_list('pub_date',
                                                                                            flat=True).first())
    prev_date = str(Book.objects.order_by('pub_date').filter(pub_date__lt=pub_date).values_list('pub_date',
                                                                                             flat=True).first())
    context = {
        'books': books,
        'next_date': next_date,
        'prev_date': prev_date,

    }
    return render(request, template, context)
