from mongoengine import *
import random
import json
import time

connect(
    db='test',
    host='mongodb://127.0.0.1:27017'
)


class Family(Document):
    name = StringField(required=True, max_length=30)
    surname = StringField(required=True)
    age = IntField(required=True)
    year_of_birth = IntField(required=True, min_value=1900, max_value=2025)
    country = StringField(default='Unknown')
    salary = StringField(default='0')
    visited_countries = ListField(StringField())


# class Test(Document):
#     value = IntField(required=True)
#     value2 = IntField(required=True)
#
#
# time1_start = time.time()
# print(Test.objects.item_frequencies('value'))
# print(Test.objects.item_frequencies('value2'))
# time1_end = time.time()
#
# time2_start = time.time()
# frequencies1 = {}
# frequencies2 = {}
# for number in Test.objects:
#     if number.value not in frequencies1:
#         frequencies1[number.value] = 1
#     else:
#         frequencies1[number.value] += 1
#
# for number in Test.objects:
#     if number.value2 not in frequencies2:
#         frequencies2[number.value2] = 1
#     else:
#         frequencies2[number.value2] += 1
# print(frequencies1)
# print(frequencies2)
# time2_end = time.time()
#
# print('===================')
#
# print(f'Скорость выполнения агрегатной функции: {round(time1_end-time1_start, 4)}')
# print(f'Скорость выполнения написанной вручную функции: {round(time2_end-time2_start, 4)}')

# for obj in Family.objects(country__in=['Russia', 'Ukraine']):
#     print(obj.name, obj.surname)


# data_list = []
# upload_list = []
# with open('data_list.txt', 'r') as file:
#     for member in file.readlines():
#         plan = {
#             'name': '',
#             'surname': '',
#             'age': '',
#             'year_of_birth': 0,
#             'country': 'Unknown',
#             'salary': '0'
#         }
#         data_list_prepare = dict()
#         for data_field in member.split(','):
#             data_field = data_field.split(':')
#             plan[data_field[0]] = data_field[1].strip('\n')
#         data_list.append(plan)
#
# for member in data_list:
#     upload_list.append(Family(name=member['name'],
#                               surname=member['surname'],
#                               age=member['age'],
#                               year_of_birth=member['year_of_birth'],
#                               country=member['country'],
#                               salary=member['salary']))
#
# for member in upload_list:
#     member.save()

# for data in data_list:
#     print(json.dumps(data, indent=4))
