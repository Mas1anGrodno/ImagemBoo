from django.contrib import admin
from .models import Category, Image




class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name", "created_at")

admin.site.register(Category,CategoryAdmin)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("file","description",'category','user', "delete", 'uploaded_at','updated_at','deleted_at')

admin.site.register(Image,ImageAdmin)
