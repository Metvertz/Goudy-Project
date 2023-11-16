from django.urls import path
from . import views

urlpatterns = [
    path('roster/', views.roster_view, name='roster'),
    path('schedule/', views.schedule_view, name='schedule'),
    path('register/', views.register, name='register'),
    path('account/', views.account_view, name='account'),
]