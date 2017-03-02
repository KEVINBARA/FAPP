from django.http import JsonResponse

from foodtaskerapp.models import Restaurant
from foodtaskerapp.serializers import RestaurantSerializer

def customer_get_restaurant(request):               #API FOR THE CUSTOMER
    restaurants = RestaurantSerializer(
        Restaurant.objects.all().order_by("id"),
        many = True,
        context = {"request":request}
    ).data

    return JsonResponse({"restaurants":restaurants})  #get all the data in the database and respond in json format
