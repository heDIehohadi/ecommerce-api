from django.db import models
from core.models import TimeStampedModel

class Brand (TimeStampedModel):
    name=models.CharField(max_length=225,unique=True, null=True, blank=True)
    slug=models.SlugField(unique=True,db_index=True)
    class Meta:
        ordering=['name']   

    def __str__(self):
        return self.name


class Category (TimeStampedModel):
    name=models.CharField(max_length=225,unique=True)
    slug=models.SlugField(unique=True,db_index=True)
    class Meta:
        ordering=['name']
        verbose_name='Category'
        verbose_name_plural='Categories'
    def __str__(self):
        return self.name
    

class Product(TimeStampedModel):
    name=models.CharField(max_length=225)
    slug=models.SlugField(unique=True,db_index=True)
    description=models.TextField()
    price=models.DecimalField(max_digits=12,decimal_places=2)
    category=models.ForeignKey(to=Category,
                               on_delete=models.PROTECT,
                               related_name='products')
    sku=models.CharField(max_length=20,unique=True)
    stock=models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/',blank=True)
    is_active=models.BooleanField(default=True)
    brand=models.ForeignKey(to=Brand,on_delete=models.PROTECT,related_name="products")
    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return self.name
