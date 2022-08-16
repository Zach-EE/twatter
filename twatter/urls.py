
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views

from apps.base.views import homepage, signup
from apps.twatfeed.views import twatfeed
from apps.twatfeed.api import api_add_twat

urlpatterns = [
    
    path('', homepage, name= 'homepage'),
    path('login/', views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    
    path('twatfeed/', twatfeed,name='twatfeed'),
    
    #API
    path('api/add_twat/', api_add_twat, name='api_add_twat'),
    #Admin
    path('admin/', admin.site.urls),
]
