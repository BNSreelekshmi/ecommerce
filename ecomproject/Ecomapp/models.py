from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=500, unique=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='catimages',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('Ecomapp:productcategory', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Products(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='prodimages',blank=True)
    stock = models.IntegerField()
    avail = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('Ecomapp:productdetail', args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)


