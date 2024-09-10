from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
#------------------------------- API ------------------------------------
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'images', ImageViewSet)

urlpatterns = [
    path("", ImagesListAll.as_view(),name='home'),
    path("<str:category_name>/", ImagesListByCategory.as_view(), name='images_by_category'),
    path('main/image_add/', AddPicture.as_view(), name='image_add'),
    path('main/image_user/', UserPictures.as_view(), name='images_user'),
    
    path('main/user/<str:user_name>/', UserInspect.as_view(), name='inspect_user'),
    path('main/user/<str:user_name>/delete/', UserDelete.as_view(), name='delete_user'),
    path('user/<str:username>/images/', SelectedUserImages.as_view(), name='selected_user_images'),
    
    path('main/image_deleted/', DeletedPictures.as_view(), name='images_deleted'),
    path('main/image_edit/<int:pk>/', EditPicture.as_view(), name='image_edit'),
    path('main/delete/<int:pk>/', DeletePicture.as_view(), name='image_delete'),
    path('main/restore/<int:pk>/', RestorePicture.as_view(), name='image_restore'),
    
#------------------------------- API ------------------------------------
    path('api/v1/', include(router.urls)),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)