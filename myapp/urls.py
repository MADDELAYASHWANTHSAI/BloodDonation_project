from django.urls import path
from .views import ( login_view, home_view, index,  blood_bank_view ,blood_stock, blood_banks, camp_schedule, camp_registration, get_districts,  success,
    
)

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('index', index, name='index'),
    path('blood_bank_view', blood_bank_view, name='blood_bank_view'),
    path('blood-bank/', blood_stock, name='blood_stock'),
    path('blood_bank_directory/', blood_banks, name="blood_banks"),
    path('camp_schedule/',camp_schedule, name='camp_schedule'),
    path('index/register/',camp_registration, name='camp_registration'),
    path('get_districts/',get_districts, name='get_districts'),
    path('success/',success, name='success'), 






]


  
    
    