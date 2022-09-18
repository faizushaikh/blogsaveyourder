
from distutils.command.upload import upload
from enum import unique
from tinymce.models import HTMLField

from django.db import models
from django.forms import IntegerField 
from django.utils.html import format_html

# Create your models here.

class Blogs_Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title= models.CharField(max_length=100)
    description=HTMLField()
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='category/',blank=True)
    add_dates=models.DateField(auto_now_add=True,null=True)

    def image_show(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%" />'.format(self.image))

    def __str__(self):
        return self.title





class Blogs_Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title= models.CharField(max_length=100)
    
    content=HTMLField()
    url=models.CharField(max_length=100)
    category=models.ForeignKey(Blogs_Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post/',blank=True)
    videos=models.FileField(upload_to="videos/",blank=True)
    add_dates=models.DateField(auto_now_add=True,null=True)


    def image_show(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%" />'.format(self.image))
 
   
      

    


