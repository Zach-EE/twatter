from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Twat
@login_required
def twatfeed(request):
    userids = [request.user.id]
    
    twats = Twat.objects.filter(created_by_id__in=userids)
    
    return render(request, 'twatfeed/twatfeed.html', {'twats': twats})
