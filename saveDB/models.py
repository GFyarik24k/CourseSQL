from django.db import models
class Student(models.Model):
    num = models.TextField(max_length=7)
    name = models.TextField()
    surname = models.TextField()
    patronymic = models.TextField()

class Coursework(models.Model):
    idStudent = models.IntegerField()
    topic_selection = models.TextField()
    selecting_sources = models.TextField()
    carrying_reserch = models.TextField()
    shaping_work = models.TextField()
    making = models.TextField()
    defending = models.TextField()
