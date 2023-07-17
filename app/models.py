from django.db import models

# Create your models here.


class Skill(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title


class Blog(models.Model):
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=155)
    description = models.TextField()
    user = models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='blogs')
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    username = models.CharField(max_length=155)
    email = models.CharField(max_length=155)
    text = models.TextField()

    def __str__(self):
        return  self.username
    