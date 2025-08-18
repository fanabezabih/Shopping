from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=28)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    Subscription = models.OneToOneField(Subscription, null=True, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    Category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    

    def __str__(self):
        return f"{self.name} price {self.price}"
