from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.login,name='login'),
    path('register/', views.register,name='register'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('logout', views.logout,name='logout'),
    path('menu/',views.menu,name='menu'),
    path('manage_users/', views.manage_users,name='manage_users'),
    path('manage_questions/', views.manage_questions,name='manage_questions'),
    path('change_password/', views.change_password,name='change_password'),
    path('add_question/',views.add_question,name='add_question'),
    path('delete_users/<pk>',views.delete_users,name='delete_users'), 
    path('delete_ques/<pk>',views.delete_ques,name='delete_ques'),    
    path('add_question_data/', views.add_question_data,name='add_question_data'),
    path('edit_ques/<pk>',views.edit_ques,name='edit_ques'),
    path('update_ques_data',views.update_ques_data,name='update_ques_data'),
    path('edit_user/<pk>',views.edit_user,name='edit_user'),
    path('update_user_data',views.update_user_data,name='update_user_data'),
    path('quiz',views.quiz,name='quiz'),
    path('result',views.result,name='result'),


 ]