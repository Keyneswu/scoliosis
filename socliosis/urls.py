from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('', views.upload_photo),  # Root URL redirects to the upload view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
