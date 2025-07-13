from django.urls import path
from .views import home_views,school_views,shop_views
urlpatterns = [
    path('',home_views.HomeView.as_view(),name='home'),
    path('school/',school_views.SchoolListView.as_view(),name='school'),
    path('shop/',shop_views.ShopListView.as_view(),name='shop')
]
