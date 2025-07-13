from shop.serializers import ShopSerializer
from api.services import  get_data,check_data
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class ShopListCreateView(APIView):
    def get(self,request):
        shop = get_data()
        serilizer = ShopSerializer(shop,many = True)
        return Response(serilizer.data, status= status.HTTP_200_OK)
    
    def post(self,request):
        serializer = ShopSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        raise Http404

class ShopUpdateDeleteView(APIView):
    
    def get(self,request,shop_id):
        shop = check_data(shop_id)
        serializer = ShopSerializer(shop)
        return Response(serializer.data,status= status.HTTP_200_OK)
    
    def put(self,request,shop_id):
        shop = check_data(shop_id)
        serializer = ShopSerializer(shop,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,shop_id):
        shop = check_data(shop_id)
        shop.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)