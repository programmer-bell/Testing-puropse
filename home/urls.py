''' This is the default urls'''
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

    # APP Endpoints
    path('',include('main.urls')),
    path('shop/',include('shop.urls')),
    path('set/',include('set.urls')),

    # API Endpoints
    path('api/v1/',include('api.urls')),
]
