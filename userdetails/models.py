from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class UserDetails(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE ) 
    photos = models.ImageField(upload_to='media/' )
    description = models.TextField()

    def __str__(self) -> str:
        return self.description[:10]




