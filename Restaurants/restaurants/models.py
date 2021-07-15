from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    describtion = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.name

 
