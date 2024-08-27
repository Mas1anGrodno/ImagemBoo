from django.shortcuts import render
from main.models import *

def home(request):
    images = Image.objects.all()

    context = {
        'title': 'All pictures',
        'images': images,
        'header': "All pictures"
        }
    return render(request, 'main/base.html', context)