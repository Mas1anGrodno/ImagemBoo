from django.db import models
from django.contrib.auth import get_user_model

class Category(models.Model):

    name = models.CharField(max_length=64, verbose_name="Image Category")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Image Category"
        verbose_name_plural = "Image Category"
        ordering = ["created_at"] # Sort by create date
    
    def __str__(self):
      return self.name

class Image(models.Model):

    file = models.ImageField(upload_to="uploads/%Y/%m/%d")
    description = models.TextField(blank=True, verbose_name='Description')
    delete = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, to_field='id',null=True,on_delete=models.SET_NULL, related_name='image_category', verbose_name="Image Category" )
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name='image_user', null = True, default=None, verbose_name="Image Uploader") 

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Image"
        ordering = ["uploaded_at"] # Sort by Upload date

    def __str__(self):
      return self.description