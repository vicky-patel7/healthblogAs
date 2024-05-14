from tkinter import CASCADE
from django.db import models

# Create your models here.
class Post(models.Model):
    sno= models.AutoField(primary_key=True)
    title= models.CharField(max_length=255)
    slug= models.CharField(max_length=150)
    content= models.TextField()
    views = models.IntegerField(default=0)
    author= models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/images', null=True, blank=True)
    timeStamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' by ' + self.author
