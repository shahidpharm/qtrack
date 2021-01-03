from typing import ChainMap
from django.db import models
from django.db.models.fields.related import ForeignKey


# Create your models here.


class Country(models.Model):
    country_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.country_name

    def __unicode__(self):
        return self.country_name


class MeasuringUnits(models.Model):
    measuring_unit_name = models.CharField(max_length=50, unique=True)
    measuring_unit_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.measuring_unit_name

    def __unicode__(self):
        return self.measuring_unit_name


class City(models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True)
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name

    def country_name(self):
        return self.country.country_name

    def __unicode__(self):
        return self.city_name


class Company(models.Model):
    company_name = models.CharField(max_length=100, null=False)
    company_code = models.CharField(max_length=30, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.company_name

    def country_name(self):
        return self.country.country_name

    def __unicode__(self):
        return self.company_name


class Plant(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    plant_name = models.CharField(max_length=30, null=False)
    plant_code = models.CharField(max_length=30, null=False)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.plant_name

    def country_name(self):
        return self.country.country_name

    def company_name(self):
        return self.company.company_name

    def __unicode__(self):
        return self.plant_name


class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null=False)
    department_name = models.CharField(max_length=50, null=False)
    department_code = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.department_name

    def company_name(self):
        return self.company.company_name

    def plant_name(self):
        return self.plant.plant_name

    def __unicode__(self):
        return self.department_name
