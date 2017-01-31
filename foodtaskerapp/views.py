from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from foodtaskerapp.forms import UserForm, RestaurantForm
from django.contrib.auth import authenticate ,login
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return redirect(restaurant_home)

@login_required(login_url = '/restaurant/sign-in/')  #if not logged in redirect to sign-in page
def restaurant_home(request):
    return render(request, 'restaurant/home.html',{})


def restaurant_sign_up(request):             #restaurant registration function

    user_form = UserForm()
    restaurant_form = RestaurantForm()

    if request.method == "POST":                                   # when a user click on the submit button
        user_form= UserForm(request.POST)
        restaurant_form = RestaurantForm(request.POST , request.FILES)      #request.Files is for the logo

    if user_form.is_valid() and restaurant_form.is_valid():
        new_user = User.objects.create_user(**user_form.cleaned_data)        #this create a new user object
        new_restaurant = restaurant_form.save(commit = False)                # this create a restaurant object but using the "commit = False" the new object wont be stored in the memory
        new_restaurant.user = new_user    #assigns the new user object to the restaurant
        new_restaurant.save()       # now the new restaurant can be stored in the database

        login(request,authenticate(
            username = user_form.cleaned_data["username"],
            password = user_form.cleaned_data["password"]
        ))

        return redirect(restaurant_home)


    return render(request, 'restaurant/sign_up.html',{ "user_form": user_form, "restaurant_form":restaurant_form })
