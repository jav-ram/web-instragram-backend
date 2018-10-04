from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=50) 
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content= models.CharField(max_length=150)
    liked= models.ManyToManyField(User, 'Like')
    likes= models.IntegerField()

class Like(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    date= models.DateTimeField(auto_now_add=True)
    
