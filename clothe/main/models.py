from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    maxTemperature = models.IntegerField(null=True, blank=True)
    minTemperature = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='colors', null=True, blank=True)

    def __str__(self):
        return self.name

class Clothes(models.Model):

    GENDER_TYPE = (
        ('Female', 'F'),
        ('Male', 'M'),
    )
    gender = models.CharField(
        max_length=8,
        choices=GENDER_TYPE,
    )

    category = models.ForeignKey(Category)
    imgUrl = models.CharField(max_length=1000)
    productUrl = models.CharField(max_length=1000)

    def __str__(self):
        return self.imgUrl


class ClothesByColor(models.Model):
    clothes = models.ForeignKey(Clothes, related_name='color_set')
    color = models.ForeignKey(Color, related_name='clothes_set')

