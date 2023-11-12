from django.urls import path
from . import views

urlpatterns=[
    path('empleados/',views.list_empl,name='list_empl'),
    path('cliente/',views.list_clien,name='list_clien'),
    path('area/',views.list_are,name='list_are'), 
    path('venta/',views.lis_ven,name='lis_ven'), 
    
]