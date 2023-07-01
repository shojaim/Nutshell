from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="دسته")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="عنوان محصول")
    price = models.IntegerField(verbose_name="قیمت محصول")
    quantity = models.PositiveIntegerField(verbose_name="چه مقدار(به گرم)")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته بندی")

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام")

    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="شهر")

    def __str__(self):
        return self.city.name

class InventoryProduct(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="نام")
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, verbose_name="انبار")
    quantity = models.PositiveIntegerField(blank=False, verbose_name="تعداد")

    def __str__(self):
        return self.name.name
    

from accounts.models import CustomUser
    
class Order(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="خریدار")
    product = models.ForeignKey(InventoryProduct, on_delete=models.CASCADE, verbose_name="محصول")
    quantity = models.PositiveIntegerField(blank=False, verbose_name="تعداد")

    SUBMITTED = 'در حال آماده سازی'
    READY_TO_SEND = 'آماده ارسال'
    STATUS_CHOICES = [
        (SUBMITTED, 'در حال آماده سازی'),
        (READY_TO_SEND, 'آماده ارسال'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=SUBMITTED, verbose_name="وضعیت")

        

