from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('',views.home),
    path('all_emp',views.all_emp),
    path('add_emp',views.add_emp),
    path('remove_emp',views.remove_emp),
    path('remove_emp/<int:emp_id>',views.remove_emp),
    path('filter_emp',views.filter_emp),
    
  
]
