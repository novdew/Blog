from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=1000)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        reverse_lazy('home')