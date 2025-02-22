from django.contrib import admin
from .models import Product
from .models import Pickle
from .models import powder
from .models import Papad
from .models import PreMix
from .models import Snacks



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_1kg', 'price_500g', 'price_250g')


@admin.register(Pickle)
class PickleAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_1kg', 'price_500g', 'price_250g')
    search_fields = ('name',)


@admin.register(powder)
class powderAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_1kg', 'price_500g', 'price_250g')
    search_fields = ('name',)



@admin.register(Papad)
class PapadAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_1kg', 'price_500g', 'price_250g')



@admin.register(PreMix)
class PreMixAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_1kg', 'price_500g', 'price_250g')



admin.site.register(Snacks)

