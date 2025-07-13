from shop.models import Shop
from django.http import Http404

def get_data():
    try:
        return Shop.objects.all()
    except Shop.DoesNotExist:
        return None
    
def check_data(shop_id):
    try:
        return Shop.objects.get(id = shop_id)
    except Shop.DoesNotExist:
        raise Http404
