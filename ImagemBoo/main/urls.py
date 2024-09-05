from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ImagesListByCategory, ImagesListAll, AddPicture, UserPictures

urlpatterns = [
    path("", ImagesListAll.as_view(),name='home'),
    path("<str:category_name>/", ImagesListByCategory.as_view(), name='images_by_category'),
    path('main/image_add/', AddPicture.as_view(), name='image_add'),
    path('main/image_user/', UserPictures.as_view(), name='images_user'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)