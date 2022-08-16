import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Twat
@login_required
def api_add_twat(request):
    data = json.loads(request.body)
    body = data['body']
    
    twat = Twat.objects.create(body=body, created_by=request.user)
    
    return JsonResponse({'success': True})