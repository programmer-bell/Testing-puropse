from django.urls import path
from.views import shops_views,schools_views
urlpatterns = [
    path('shop/',shops_views.ShopListCreateView.as_view(),name='shop_list_create'),
    path('shop/<int:shop_id>/',shops_views.ShopUpdateDeleteView.as_view(),name='shop_update_delete'),
    path('school/',schools_views.SchoolListCreateView.as_view(),name='school_list'),
    path('school/<int:pk>/',schools_views.SchoolUpdateDeleteView.as_view(),name='school_update_delete'),
]
