from django.urls import path
from .views import StaffList, StaffDetail

urlpatterns = [
    path('', StaffList.as_view()),
    path('<int:id>', StaffDetail.as_view())
]