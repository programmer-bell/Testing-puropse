from django.shortcuts import render
from main.services import get_data_school
from django.views import View

class SchoolListView(View):
    def get(self,request):
        school = get_data_school()
        context = {
            'school':school
        }
        return render(request,'school.html',context)