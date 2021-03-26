#models.py
from django.db import models
 
# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=40)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    bio = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return self.firstname + " " + self.lastname
 
    class Meta:
        ordering = ['created']
   
    class Meta:  
        db_table = "blog_member"