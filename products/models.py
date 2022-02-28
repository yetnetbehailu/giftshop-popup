from django.db import models
from django.core.validators import RegexValidator


class Category(models.Model):
    """ Categorize according to product sort"""
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return str(self.friendly_name)


class Product(models.Model):
    """ Store products model """
    SUB_CATEGORY_CHOICES = [
        ('oil_painting', 'Oil Painting'),
        ('impasto_painting', 'Impasto Painting'),
        ('line_art', 'Line Art'),
    ]

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sub_category = models.CharField(
        max_length=20, choices=SUB_CATEGORY_CHOICES, null=True,
        blank=True, default=False)
    name = models.CharField(max_length=254)
    artist = models.CharField(max_length=254, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True,
                                 blank=True)
    width = models.CharField(
        max_length=4, null=True, blank=True,
        validators=[RegexValidator(r'^\d[0-9]$')])
    height = models.CharField(
        max_length=4, null=True, blank=True,
        validators=[RegexValidator(r'^\d[0-9]$')])
    in_stock = models.BooleanField(default=True, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
