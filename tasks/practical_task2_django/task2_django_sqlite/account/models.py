from django.db import models

director = 'DI'
designer = 'DG'
cleaner = 'CL'
admin = 'AD'
user = 'UR'

POSITIONS = [
    (director, 'Директор'),
    (designer, 'Дизайнер'),
    (cleaner, 'Уборщик'),
    (admin, 'Администратор'),
    (user, 'Пользователь'),
]


# Create your models here.
class Order(models.Model):
    pass


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)


class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=2,
                                choices=POSITIONS,
                                default=user)
    labor_contract = models.IntegerField()


class ProductOrder(models.Model):
    pass


