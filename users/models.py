
#Django
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    """Profile model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length = 200, blank = True)
    biograpgy = models.TextField(blank = True)
    phone_number = models.CharField(max_length = 30, blank = True)

    picture = models.ImageField(upload_to='users/picture', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username
