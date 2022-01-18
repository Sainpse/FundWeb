from django.db import models

# Create your models here.
# Use this sites simple database models to enable quick text or any other content update without having to change the html code

class USERS(models.Model):
    firstName  = models.CharField(max_length=20)
    lastName   = models.CharField(max_length=20)
    email      = models.EmailField(max_length=50)


    
    