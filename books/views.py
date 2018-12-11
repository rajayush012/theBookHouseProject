from django.shortcuts import render
from .models import Books
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    books = Books.objects
    return render(request,'books/home.html',{'books':books})

def bookdet(request, book_id):
    bookin = get_object_or_404(Books,pk=book_id)
    return render(request,'books/detail.html',{'book':bookin})
