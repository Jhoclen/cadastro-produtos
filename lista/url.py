



from django.contrib import admin
from django.urls import path,include
from .views import home,colunas,deletar

urlpatterns = [
    
    path('save',home),
    path('lista',colunas),
    path('deletar/<int:id>/',deletar)
    
]
