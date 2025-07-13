from school.models import School
from shop.models import Shop

def get_data_school():
    try:
        return School.objects.all()
    except School.DoesNotExist:
        return None

def get_data_shop():
    try:
        return Shop.objects.all()
    except Shop.DoesNotExist:
        return None