from django.urls import path
from .views import (
    StaffList, StaffDetail, StaffCreate, StaffUpdate, StaffDelete
)

urlpatterns = [
    path('', StaffList.as_view(), name='full_list'),
    path('<int:id>', StaffDetail.as_view(), name='employee'),
    path('create/', StaffCreate.as_view(), name='staff_add'),
    path('<int:id>/update/', StaffUpdate.as_view(), name='staff_update'),
    path('<int:id>/delete/', StaffDelete.as_view(), name='staff_delete'),
]