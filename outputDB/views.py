from django.shortcuts import render
from django.http import HttpResponse
from saveDB.func import *

def queryGetStudent(request):
    num = request.GET.get("num")
    name = request.GET.get("name")
    surname = request.GET.get("surname")
    patronymic = request.GET.get("patronymic")

    student = getStudent(num,name,surname,patronymic)

    print(student)
    return HttpResponse((f"ID студента: {obj.id} - №Студ.: {obj.num},"
                                f" ФИО: {obj.name} {obj.surname} {obj.patronymic}<br>" for obj in student)
        if len(student) else f"Студента не существует в базе")