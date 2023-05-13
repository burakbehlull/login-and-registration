from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    #password?
    created = models.DateTimeField(auto_now_add=True)
