"""foodtasker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from foodtaskerapp import views , apis
from django.contrib.auth import views as auth_views  #authenctication library of django


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home,name = 'home'),
    url(r'^restaurant/sign-in/$',auth_views.login, {'template_name': 'restaurant/sign_in.html'}, name = 'restaurant-sign-in'), #we will create a new page for sign in
    url(r'^restaurant/sign-out/$', auth_views.logout,{'next_page': '/'}, name = 'restaurant-sign-out'), # '/' redirect to the homepage
    url(r'^restaurant/sign-up/$', views.restaurant_sign_up, name = 'restaurant-sign-up'),
    url(r'^restaurant/$',views.restaurant_home,name = 'restaurant-home'),

    #general structure for the restaurant'dashboard

    url(r'^restaurant/account/$', views.restaurant_account , name = 'restaurant-account'),
    url(r'^restaurant/meal/$', views.restaurant_meal , name = 'restaurant-meal'),
    url(r'^restaurant/meal/add/$', views.restaurant_add_meal , name = 'restaurant-add-meal'),
    url(r'^restaurant/meal/edit/(?P<meal_id>\d+)/$', views.restaurant_edit_meal , name = 'restaurant-edit-meal'),
    url(r'^restaurant/order/$', views.restaurant_order , name = 'restaurant-order'),
    url(r'^restaurant/report/$', views.restaurant_report , name = 'restaurant-report'),

    #Sign In/Sign Up/Sign Out
    url(r'^api/social/', include('rest_framework_social_oauth2.urls')),
    # /convert-token (sign-in /sign-up)
    #/revoke-token (sign-out)


    url(r'^api/customer/restaurant/$', apis.customer_get_restaurant),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
