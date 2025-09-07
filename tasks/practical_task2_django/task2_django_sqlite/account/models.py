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


class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=2,
                                choices=POSITIONS,
                                default=user)
    labor_contract = models.IntegerField()


# Create your models here.
class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0)
    pickup = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through='ProductOrder')


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

