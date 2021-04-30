from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='landing'),
    path('role-index',views.roles_index,name='role-index'),
    path('personnel-home',views.personnel_index, name='personnel-home'),
    path('department-index',views.department_index,name='department-index'),
]