from django.urls import URLPattern, path
from base.views import user_views as views

from rest_framework_simplejwt.views import (
    TokenObtainPairView)


urlpatterns = [

    path('/login', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path("/Profile", views.getUserProfile, name="UserProfile"),
    path("/Update", views.updateUserProfile, name="updateUserProfile"),
    path("", views.getUsers, name="Users"),
    path("/registerUsers", views.registerUsers, name="registerUsers"),

]
