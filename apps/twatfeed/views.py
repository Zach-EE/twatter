from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def twatfeed(request):
    return render(request, 'twatfeed/twatfeed.html')
