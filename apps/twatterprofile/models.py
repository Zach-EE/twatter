from django.contrib.auth.models import User
from django.db import models

class TwatterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

User.twatterprofile = property(lambda u:TwatterProfile.objects.get_or_create(user=u)[0])