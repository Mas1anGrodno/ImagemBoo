from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from main.models import *

class ImagesListAll(ListView):
    model = Image
    template_name = 'main/image_view.html'

    def get_queryset(self):
        return Image.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ImagemBoo - All Images'
        return context
    
class ImagesList(ListView):
    model = Image
    template_name = 'main/image_view.html'

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = get_object_or_404(Category, name=category_name)
        return Image.objects.filter(category=category)