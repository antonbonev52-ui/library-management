from django.shortcuts import render
from .models import Author


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})


from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
