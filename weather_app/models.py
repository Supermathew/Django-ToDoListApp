from django.db import models
from django.contrib.auth.models import User

class Todolist(models.Model):
    manage=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    id = models.AutoField(primary_key=True)
    task=models.CharField(max_length=300)
    done=models.BooleanField(default=False)

    def __str__(self):
        return self.task

class Contact(models.Model):
    manage=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=300)
    email=models.EmailField(max_length=254)
    message= models.CharField(max_length=350)

    def __str__(self):
        return self.message


