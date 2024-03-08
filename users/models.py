from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):    
    email = models.EmailField(unique=True)

    # Add custom fields here, if needed
    def __str__(self):
        return self.username
