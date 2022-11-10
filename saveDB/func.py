from .models import *
from django.db import connection
def addStudent (num, name, surname, patronymic):
    student = Student(num=num, name=name, surname=surname, patronymic=patronymic)
    student.save()
    return student

def getStudent (num, name, surname, patronymic):
    try:
        student = Student.objects.filter(num__icontains=num) & \
               Student.objects.filter(name__icontains=name) & \
               Student.objects.filter(surname__icontains=surname) & \
               Student.objects.filter(patronymic__icontains=patronymic)
    except Student.DoesNotExist:
        student = None

    return student

# def addStudent(num, name, surname, patronymic):
#     student = Student(num=num, name=name, surname=surname, patronymic=patronymic)
#     student.save()
#     return student
#
# def getStudent(num, name, surname, patronymic):
#     try:
#         student = Student.objects.filter(num__icontains=num) & \
#                   Student.objects.filter(name__icontains=name) & \
#                   Student.objects.filter(surname__icontains=surname) & \
#                   Student.objects.filter(patronymic__icontains=patronymic)
#     except Student.DoesNotExist:
#         student = None
#
#     return student