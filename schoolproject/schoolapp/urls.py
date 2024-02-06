
from . import views
from django.urls import path,include

from django.http import JsonResponse





app_name='schoolapp'
urlpatterns = [
    path('', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('new_page/', views.new_page, name='new_page'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'), # AJ
    path('logout_view/', views.logout_view, name='logout_view'),
    path('confirm_view/', views.confirm_view, name='confirm_view'),
  



]

