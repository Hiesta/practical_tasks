from mongoengine import *

connect(
    db='test',
    host='mongodb://127.0.0.1:27017'
)

employee_fields = ['name', 'surname', 'age', 'salary', 'job']


class Employee(Document):
    name = StringField(required=True, default='TBA')
    surname = StringField(required=True, default='TBA')
    age = IntField(required=True, min_value=18, default=504)
    salary = IntField(required=True, min_value=0, default=504)
    job = StringField(required=True, default='TBA')


def new_employee_data():
    new_employee = {}
    for field in employee_fields:
        new_employee[field] = input(f"Введите {field} сотрудника:\t")
    return new_employee


def filter_func(data):
    if data == '0':
        get_data_from_db()
    elif data == '1':
        user = input('1+ - по возрастанию зарплаты\n'
                     '1- - по убыванию зарплаты\n'
                     '2+ - по возрастанию возраста\n'
                     '2- - по убыванию возраста\n')
        if user == '1+':
            get_data_order_by('salary')
        elif user == '1-':
            get_data_order_by('-salary')
        elif user == '2+':
            get_data_order_by('age')
        elif user == '2-':
            get_data_order_by('-age')
    elif data == '2':
        user = input('1 - по имени\n'
                     '2 - по фамилии\n'
                     '3 - по возрасту\n'
                     '4 - по должности\n')
        if user == '1':
            name = input('Имя:\t')
            get_data_from_db({'name': name})
        if user == '2':
            surname = input('Фамилия:\t')
            get_data_from_db({'surname': surname})
        if user == '3':
            age = input('Возраст:\t')
            get_data_from_db({'age': age})
        if user == '4':
            job = input('Должность:\t')
            get_data_from_db({'job': job})


def get_data_from_db(_filter: dict = ''):
    try:
        result = Employee.objects(**_filter)
        for employee in result:
            print(employee.name, employee.surname, employee.age, employee.salary, employee.job)
    except Exception as e:
        print(f'Произошла ошибка {str(e)}')


def get_data_order_by(_filter):
    result = Employee.objects().order_by(_filter)


def add_new_employee(employee):
    try:
        new = Employee(**employee)
        new.save()
        print('Данные о сотруднике успешно введены в базу данных\n')
    except Exception as e:
        print('Произошла ошибка', str(e))


if __name__ == '__main__':
    user_input = input('Выберите действие:\n'
                       '1 - добавить данные о сотруднике\n'
                       '2 - получить данные о сотрудниках\n'
                       '0 - Выход\n')
    while user_input != '0':
        if user_input == '1':
            add_new_employee(new_employee_data())
        else:
            fltr = input("Введите:\n"
                         "0 - если хотите вывести всех сотрудников без фильтра\n"
                         "1 - вывести в возрастании или убывании зарплаты или возраста\n"
                         "2 - найти по данным\n")
            filter_func(fltr)
        user_input = input('Выберите действие:\n'
                           '1 - добавить данные о сотруднике\n'
                           '2 - получить данные о сотрудниках\n'
                           '0 - Выход\n')
