from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from apps.twatfeed.models import Twat

def homepage(request):
    twats = Twat.objects.all()
    return render(request, 'base/homepage.html',{'twats': twats})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login (request,user)
            
            return redirect('homepage')
    else:
        form = UserCreationForm()
        # context = {
        #     'form': form,
        # }
        
    return render(request, 'base/signup.html', {'form': form})
