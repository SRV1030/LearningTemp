from django.db import models

class info(models.Model):
    name= models.CharField(max_length=250,unique='True')
    details= models.TextField();

    def __str__(self):
        return self.name

class webs(models.Model):
    namew= models.ForeignKey(info)
    webpage = models.URLField(unique='True')
    email = models.EmailField()
    def __str__(self):
        return self.namew




# Create your models here.
