from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.db.models.aggregates import Avg

FLAG_TYPES = (
    ('Sale','Sale'),
    ('New','New'),
    ('Feature','Feature'),
 )

# Create your models here.
class Product(models.Model):
    name = models.CharField(_("Name"), max_length=120)
    flag = models.CharField(_("Flag"), choices=FLAG_TYPES, max_length=10)
    image = models.ImageField(_("Image"), upload_to='products')
    price = models.FloatField(_("Price"))
    sku = models.CharField(_("Sku"), max_length=50)
    subtitle = models.CharField(_("Subtitle"), max_length=300)
    tag = TaggableManager(_("Tag"))
    descriptions = models.TextField(_("Descriptions"), max_length=40000)
    quantity = models.IntegerField(_("Quantity"))
    brand = models.ForeignKey("Brand", verbose_name=('Brand'), related_name='product_brand', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(_("Slug"), null=True, blank=True)
    create_at = models.DateTimeField(_("Create at"), default=timezone.now, null=True, blank=True)

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    # def ave_rate(self):
    #       avg = self.review_product.aggregate(rate_ave=Avg('rate'))
    #       return avg['rate_ave']
    
    def __str__(self) -> str:
            return self.name
    



class ProductImages(models.Model):
    products = models.ForeignKey(Product, related_name='product_image', verbose_name=_("Product"), on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to='product_images')

    def __str__(self) -> str:
                return str(self.products)


class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    image = models.ImageField(_("Images"), upload_to='brand')
    slug = models.SlugField(_("Slug"), null=True, blank=True)


    def __str__(self) -> str:
            return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)
    

class Review(models.Model):
    user = models.ForeignKey(User, verbose_name=('User'), related_name='rebiew_user', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, related_name='review_product', verbose_name=_("Product"), on_delete=models.SET_NULL, null=True)
    rate = models.IntegerField(_("Rate"))
    review = models.CharField(_("Review"), max_length=300)
    create_at = models.DateTimeField(_("Create at"), default=timezone.now)


    def __str__(self) -> str:
            return f"{self.user} - {self.product}"