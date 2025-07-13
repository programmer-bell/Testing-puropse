from django.shortcuts import render
from django.views import View
from main.services import *
# Create your views here.
class HomeView(View):
    def get(self, request):
        school = get_data_school()
        shop = get_data_shop()
        context = {
            'shop': shop,
            'school': school
        }
        return render(request, 'home.html', context)
