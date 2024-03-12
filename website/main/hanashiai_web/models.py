from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser 


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now) 
    image = models.ImageField(null=True, blank=True, upload_to="images/" )

    def __str__(self):
        return self.title + ' | ' + str(self.author) 
    

    def get_absolute_url(self):
        return reverse('post_details', kwargs={"pk": self.id}) 

class Comments(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE )
    author = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
  
    def __str__(self):
        return str(self.author) 
    
    def get_absolute_url(self):
        return reverse('post_details', kwargs={"pk": self.post.id})




    








