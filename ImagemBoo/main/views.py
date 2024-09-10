from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import *
from .forms import *

class ImagesListAll(ListView):
    model = Image
    template_name = 'main/image_view.html'

    def get_queryset(self):
        return Image.objects.filter(delete=False)
    
class ImagesListByCategory(ListView):
    model = Image
    template_name = 'main/image_view.html'

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category_selected = get_object_or_404(Category, name=category_name)
        return Image.objects.filter(category=category_selected, delete=False)
    
class AddPicture(CreateView):
    model = Image
    template_name = 'main/image_add.html'
    fields = ['file', 'description', 'category']
    success_url = reverse_lazy('images_user')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditPicture(UpdateView):
    model = Image
    template_name = 'main/image_edit.html'
    fields = ['description', 'category']
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image'] = self.object
        context['form'] = self.get_form()
        return context

class DeletePicture(UpdateView):
    model = Image
    fields = ['delete']
    template_name = 'main/image_confirm.html'
    success_url = reverse_lazy('images_user') 

    def form_valid(self, form):
        form.instance.delete = True
        return super().form_valid(form)

class RestorePicture(UpdateView):
    model = Image
    fields = ['delete']
    template_name = 'main/image_confirm.html'
    success_url = reverse_lazy('images_user') 

    def form_valid(self, form):
        form.instance.delete = False
        return super().form_valid(form)
    
class UserPictures(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'main/image_user.html'

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user, delete=False)
class SelectedUserImages(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'main/image_selected_user.html'

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['username'])
        return Image.objects.filter(user=user, delete=False)
    
class DeletedPictures(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'main/image_deleted.html'

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user, delete=True)

class UserInspect(UpdateView):
    model = User
    form_class = UserInspectForm
    template_name = 'main/user_inspect.html'
    success_url = reverse_lazy('images_user')

    def get_object(self, queryset=None):
        return User.objects.get(username=self.kwargs['user_name'])

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        if password:
            user.set_password(password)
        user.save()
        return super().form_valid(form)
    
class UserDelete(DeleteView):
    model = User
    template_name = 'main/user_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return User.objects.get(username=self.kwargs['user_name'])