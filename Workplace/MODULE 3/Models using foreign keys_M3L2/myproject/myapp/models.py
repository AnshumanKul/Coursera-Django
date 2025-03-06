from django.db import models

# Create your models here.
class Drinkscategory(models.Model):
    categoryname=models.CharField(max_length=200)

class Drinks(models.Model):
    drink=models.CharField(max_length=200)
    price=models.IntegerField(null=False)
    category_id=models.ForeignKey(Drinkscategory,on_delete=models.PROTECT,default=None)
    
    