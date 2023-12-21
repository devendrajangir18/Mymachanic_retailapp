from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin = models.IntegerField() 
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# class Register(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=100)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name