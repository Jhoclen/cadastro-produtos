



from django.contrib import admin
from django.urls import path,include
from lista.views import home,colunas,inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/',include('lista.url')),
    path('',inicio)
    
    
]
