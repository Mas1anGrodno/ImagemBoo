from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ImagesList, ImagesListAll

urlpatterns = [
    path("", ImagesListAll.as_view(),name='home'),
    path("<str:category_name>/", ImagesList.as_view(), name='images_by_category'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)