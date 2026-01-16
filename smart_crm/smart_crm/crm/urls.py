from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('customers/', views.customer_list, name='customer_list'),
    path('add_lead/', views.add_lead, name='add_lead'),
    path('leads/', views.lead_list, name='lead_list'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
