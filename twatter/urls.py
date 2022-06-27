
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views

from apps.base.views import homepage, signup
urlpatterns = [
    
    path('', homepage, name= 'homepage'),
    path('login/', views.LoginView.as_view(template_name='base/login'), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    path('admin/', admin.site.urls),
]
