from django.contrib import admin
from .models import Country, MeasuringUnits, City, Company, Plant, Department


# Register your models here.
class MeasuringUnitAdmin(admin.ModelAdmin):
    list_display = ('measuring_unit_name', 'measuring_unit_code')


class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'country_name')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_code', 'country_name')


class PlantAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'plant_name', 'plant_code', 'country_name')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'plant_name',
                    'department_name', 'department_code')


admin.site.register(Country)
admin.site.register(MeasuringUnits, MeasuringUnitAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Plant, PlantAdmin)
admin.site.register(Department, DepartmentAdmin)
