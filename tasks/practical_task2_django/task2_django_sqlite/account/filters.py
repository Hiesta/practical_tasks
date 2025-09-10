from django_filters import FilterSet
from .models import Staff, Product


class StaffFilter(FilterSet):
    class Meta:
        model = Staff
        fields = {
            'full_name': ['icontains'],
            'salary': [
                'gt',
                'lt',
            ],
            'age': ['exact'],
        }
