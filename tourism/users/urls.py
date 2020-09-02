from django.urls import path
from .views import registration_view,userdetails,updateuser
from rest_framework.authtoken.views import obtain_auth_token

app_name = "users"
urlpatterns = [
    path("register",registration_view,name = "register"),
    path("login",obtain_auth_token,name = "login"),
    path("details",userdetails,name = "details"),
    path("details/update",updateuser,name = "update")     
    
]