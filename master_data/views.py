from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Country, Company, City, MeasuringUnits, Plant
from .forms import CountryForm, CityForm, MeasuringUnitForm, CompanyForm, PlantForm


# Create your views here.
def index(request):
    return render(request, 'home.html')


def country(request):
    country = Country.objects.all()

    context = {'country': country,
               }
    return render(request, 'master_data/country/country_list.html', context)


def country_add(request):
    form = CountryForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        form.save()
        return redirect('/master_data/country')

    return render(request, 'master_data/country/country_add.html', {'form': form})


def city(request):
    city = City.objects.all()

    context = {'country': country,
               'city': city
               }
    return render(request, 'master_data/city/city_list.html', context)


def city_add(request):
    form = CityForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        form.save()
        return redirect('/master_data/city')

    return render(request, 'master_data/city/city_add.html', {'form': form})


def measuring_unit(request):
    measuring_unit = MeasuringUnits.objects.all()

    context = {'measuring_unit': measuring_unit,
               }
    return render(request, 'master_data/measuring_unit/measuring_unit_list.html', context)


def measuring_unit_add(request):
    form = MeasuringUnitForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        form.save()
        return redirect('/master_data/measuring_unit')

    return render(request, 'master_data/measuring_unit/measuring_unit_add.html', {'form': form})


def company(request):
    company = Company.objects.all()

    context = {'country': country,
               'company': company
               }
    return render(request, 'master_data/company/company_list.html', context)


def company_add(request):
    form = CompanyForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        form.save()
        return redirect('/master_data/company')

    return render(request, 'master_data/company/company_add.html', {'form': form})


def plant(request):
    plant = Plant.objects.all()

    context = {'country': country,
               'company': company,
               'plant': plant
               }
    return render(request, 'master_data/plant/plant_list.html', context)


def plant_add(request):
    form = PlantForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        form.save()
        return redirect('/master_data/plant')

    return render(request, 'master_data/plant/plant_add.html', {'form': form})


# AJAX
def load_company(request):
    country_id = request.GET.get('country')
    companies = Company.objects.filter(country_id=country_id).order_by('company_name')
    return render(request, 'master_data/company_dropdown_list_options.html', {'companies': companies})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
