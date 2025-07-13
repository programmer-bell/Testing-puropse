from django.shortcuts import render
from main.services import get_data_shop
from django.views import View

class ShopListView(View):
    def get(self,request):
        shop = get_data_shop()
        context = {
            'shop':shop
        }
        return render(request,'shop.html',context)