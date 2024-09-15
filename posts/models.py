from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f"{self.title} | by: {str(self.author)}"
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug}) 
    
    def save(self, *args, **kwargs):
       self.slug = slugify(self.title.lower(), allow_unicode=True)
       self.title = self.title.title()
       super().save(*args, **kwargs)
