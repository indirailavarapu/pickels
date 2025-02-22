from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_1kg = models.DecimalField(max_digits=10, decimal_places=2)
    price_500g = models.DecimalField(max_digits=10, decimal_places=2)
    price_250g = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name
    





from django.db import models

class Pickle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='pickles/')
    price_1kg = models.DecimalField(max_digits=10, decimal_places=2)
    price_500g = models.DecimalField(max_digits=10, decimal_places=2)
    price_250g = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Pickle, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=50)  # 1kg, 500g, 250g

    def __str__(self):
        return f"{self.quantity} x {self.product.name} ({self.size})"



class powder(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='powder/')
    price_1kg = models.DecimalField(max_digits=10, decimal_places=2)
    price_500g = models.DecimalField(max_digits=10, decimal_places=2)
    price_250g = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    

class Papad(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='papads/')
    price_1kg = models.DecimalField(max_digits=6, decimal_places=2)
    price_500g = models.DecimalField(max_digits=6, decimal_places=2)
    price_250g = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name



class Snacks(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_1kg = models.DecimalField(max_digits=6, decimal_places=2)
    price_500g = models.DecimalField(max_digits=6, decimal_places=2)
    price_250g = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='snacks_images/')

    def __str__(self):
        return self.name



class PreMix(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='premixes/')
    price_1kg = models.DecimalField(max_digits=6, decimal_places=2)
    price_500g = models.DecimalField(max_digits=6, decimal_places=2)
    price_250g = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name



