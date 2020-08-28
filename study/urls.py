from django.urls import path

from . import views

app_name = 'study'
urlpatterns = [
    path('', views.index, name='index'),
    path('activitiy/<int:id>/', views.activity, name='activity'),
]
