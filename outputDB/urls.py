from django.urls import path
from app.outputDB import views

urlpatterns = [
    path('getStudentCourse', views.queryGetStudentCourse),
    path('addStudentCourse', views.queryAddStudentCourse)
]