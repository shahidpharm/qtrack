from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('master_data/country', country, name='country'),
    path('master_data/country/add', country_add, name='country_add'),
    path('master_data/city', city, name='city'),
    path('master_data/city/add', city_add, name='city_add'),
    path('master_data/measuring_unit', measuring_unit, name='measuring_unit'),
    path('master_data/measuring_unit/add', measuring_unit_add, name='measuring_unit_add'),
    path('master_data/company', company, name='company'),
    path('master_data/company/add', company_add, name='company_add'),
    path('master_data/plant', plant, name='plant'),
    path('master_data/plant/add', plant_add, name='plant_add'),
    path('ajax/load-companies/', load_company, name='ajax_load_companies'), # AJAX
]
