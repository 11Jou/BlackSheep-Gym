from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('signup/', include('signup.urls')),
    path('clsses/', include('classes.urls')),
    path('offers/', include('offer.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
