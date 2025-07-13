from django.shortcuts import render
from django.views import View
from .forms import ReservationForm,MenuItemForm
from django.http import HttpResponse

class HomeView(View):
    def get(self,request):
        return render(request,'set/index.html')
    
def home(request):
    form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Sucess")
        
    return render(request,'set/index.html',{'form':form})

from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import MenuItemForm  # Assuming you have a MenuItemForm

class MenuItemView(View):
    def post(self, request):
        menu_form = MenuItemForm(request.POST)
        if menu_form.is_valid():
            menu_form.save()
            return HttpResponse('Success')
        return render(request, 'set/home.html', {'form': menu_form})  # Use 'form' as the key

    def get(self, request):
        form = MenuItemForm()  # Instantiate the form for the GET request
        return render(request, 'set/home.html', {'form': form})
