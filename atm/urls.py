from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),  
    path('dashboard/', views.dashboard, name='dashboard'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('transfer/', views.transfer, name='transfer'),
    path('success/', views.success_page, name='success'),
    path('mini-statement/', views.mini_statement, name='mini_statement'),
    path('change-pin/', views.change_pin, name='change_pin'),
    path('logout/', views.logout_view, name='logout'),
]
