from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from datetime import datetime
from .resources import POSITIONS


class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    position = models.CharField(max_length=2,
                                choices=POSITIONS,
                                default='UR')
    labor_contract = models.IntegerField()
    salary = models.IntegerField(default=0,
                                 blank=True)

    def get_absolute_url(self):
        return reverse('employee', args=[str(self.id)])

    # Если вернуться на страницу всех сотрудников:
    # def get_absolute_url(self):
    #   return reverse_lazy('full_list')

    def get_last_name(self):
        data = self.full_name.split()
        surname = f'{data[0]}'
        return surname

    def __str__(self):
        return self.full_name


# Create your models here.
class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0)
    pickup = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through='ProductOrder')

    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()

    def get_duration(self):
        if self.complete:
            return (self.time_out - self.time_in).total_seconds()
        else:
            return (datetime.now() - self.time_in).total_seconds()


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.name}'


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    _amount = models.IntegerField(default=1, db_column='amount')

    def product_sum(self):
        product_price = self.product.price
        return product_price * self.amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value >= 0:
            self._amount = int(value)
        else:
            self._amount = 0
        self.save()
