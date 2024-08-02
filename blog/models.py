from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    images = models.ImageField(upload_to='blog/images/')
    title = models.CharField(max_length=55)
    likes = models.PositiveIntegerField(default = 0)
    draft = models.BooleanField(default=False)
    is_published = models.DateTimeField(auto_now=True)