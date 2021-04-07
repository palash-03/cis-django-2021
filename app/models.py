from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
	name=models.CharField(max_length=100)

	def __str__(self):
		return self.name

class TaggList(models.Model):
	tagg_name=models.CharField(max_length=100)
	
	def __str__(self):
		return self.tagg_name

class Product(models.Model):
	owner=models.ForeignKey(User,on_delete=models.CASCADE)
	product_name=models.CharField(max_length=100)
	tags=models.ManyToManyField(TaggList)
	image=models.ImageField(upload_to='product/image')
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	discription=models.TextField()

	def __str__(self):
		return f'{self.product_name}'
