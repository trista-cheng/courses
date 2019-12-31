from django.contrib import admin

# Register your models here.
from .models import Color, ClothesByColor, Clothes, Category

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'img']

@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('category', 'imgUrl', 'productUrl')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'minTemperature', 'maxTemperature')

@admin.register(ClothesByColor)
class ClothesByColorAdmin(admin.ModelAdmin):
    list_display = ('clothes', 'color')
