from django.urls import path, include

urlpatterns = [
    path('requestDB/', include('outputDB.urls')),
    path('api/', include('api.urls'))
]
