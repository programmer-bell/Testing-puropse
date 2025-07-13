from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('reservation/',views.home),
    path('menuitem/', views.MenuItemView.as_view(), name='menu'),
]
