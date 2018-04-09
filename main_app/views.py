from django.shortcuts import render
# from django.http import HttpResponse
from .models import Book


# Create your views here
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'detail.html', {'book': book})
# class Book:
#     def __init__(self, name, author, pages, description, rating, img_url):
#         self.name = name
#         self.author = author
#         self.pages = pages
#         self.description = description
#         self.rating = rating
#         self.img_url = img_url
# books = [
#     Book('Imię Róży', 'Umberto Eco', 500, 'Opis tej przezacnej książki', 10, 'https://www.wydawnictwoliterackie.pl/resources/5/17427-n-a.jpg'),
#     Book('Krótka Historia Czasu', 'Stephen Hawking', 200, 'Krótko i na temat', 8, 'https://www.wydawnictwoliterackie.pl/resources/5/17427-n-a.jpg'),
#     Book('Automate Boring Stuff with Python', 'Unknown', 750, 'Yep', 8, 'https://www.wydawnictwoliterackie.pl/resources/5/17427-n-a.jpg')
# ]