from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def homepage(request):
    return render(request, 'base/homepage.html')


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
