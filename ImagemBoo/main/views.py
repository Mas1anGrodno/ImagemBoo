from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import *

class ImagesListAll(ListView):
    model = Image
    template_name = 'main/image_view.html'

    def get_queryset(self):
        return Image.objects.all()
    
class ImagesListByCategory(ListView):
    model = Image
    template_name = 'main/image_view.html'

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category_selected = get_object_or_404(Category, name=category_name)
        return Image.objects.filter(category=category_selected)
    
class AddPicture(CreateView):
    model = Image
    template_name = 'main/image_add.html'
    fields = ['file', 'description', 'category']
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UserPictures(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'main/image_view.html'

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)