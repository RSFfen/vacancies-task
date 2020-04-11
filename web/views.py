from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Vacancy, Company, Specialty


# Create your views here.
class MainPageView(View):
    def get(self, request, *args, **kwargs):
        specialties1 = []
        for i in range(0, 4):
            dc = {}
            specialty = Specialty.objects.all()[i]
            dc['id'] = specialty.id
            dc['code'] = specialty.code
            dc['picture'] = specialty.picture
            dc['total_vacs'] = Vacancy.objects.filter(specialty=specialty.id).count()
            specialties1.append(dc)
        specialties2 = []
        for i in range(4, 8):
            dc = {}
            specialty = Specialty.objects.all()[i]
            dc['id'] = specialty.id
            dc['code'] = specialty.code
            dc['picture'] = specialty.picture
            dc['total_vacs'] = Vacancy.objects.filter(specialty=specialty.id).count()
            specialties2.append(dc)

        companies1 = []
        for i in range(0, 4):
            dc = {}
            company = Company.objects.all()[i]
            dc['id'] = company.id
            dc['logo'] = company.logo
            dc['total_vacs'] = Vacancy.objects.filter(company=company.id).count()
            companies1.append(dc)

        companies2 = []
        for i in range(4, 8):
            dc = {}
            company = Company.objects.all()[i]
            dc['id'] = company.id
            dc['logo'] = company.logo
            dc['total_vacs'] = Vacancy.objects.filter(company=company.id).count()
            companies2.append(dc)

        return render(request, 'web/index.html', context=
        {'title': 'Джуманджи', 'specialties1': specialties1, 'specialties2': specialties2,
         'companies1': companies1, 'companies2': companies2, })


class SpecialtyVacanciesView(View):
    def get(self, request, code, *args, **kwargs):
        specialty_codes = Specialty.objects.filter(code=code).values('code')
        #        print(specialty_codes)
        if specialty_codes == None:
            raise Http404
        specialty = Specialty.objects.filter(code=code).last()
        title = specialty.title
        picture = specialty.picture

        sp_vacancies = Vacancy.objects.filter(specialty_id=specialty.id)
        total_vacs = sp_vacancies.count()
        sp_vac = []
        for i in range(total_vacs):
            dc = {}
            spv = sp_vacancies[i]
            dc['id'] = spv.id
            dc['title'] = spv.title
            dc['specialty_title'] = title
            co = Company.objects.filter(name=spv.company).last()
            #            print("co_pk", co.pk)
            dc['company_id'] = co.pk
            dc['company_logo'] = co.logo
            dc['skills'] = spv.skills
            dc['description'] = spv.description
            dc['salary_min'] = spv.salary_min
            dc['salary_max'] = spv.salary_max
            dc['published_at'] = spv.published_at
            sp_vac.append(dc)

        return render(request, 'web/vacancies_sp.html', context=
        {'title': title, 'picture': picture, 'total_vacs': total_vacs,
         'vacancies': sp_vac, })


class CompanyView(View):
    def get(self, request, pk, *args, **kwargs):
        company = get_object_or_404(Company, pk=pk)
        if company is None:
            raise Http404
        title = company.name
        logo = company.logo
        location = company.location
        employee_count = company.employee_count
        description = company.description

        co_vacancies = Vacancy.objects.filter(company=pk)
        #        print(co_vacancies)
        total_vacs = co_vacancies.count()

        return render(request, 'web/vacancies_co.html',
                      context={'title': title, 'logo': logo, 'total_vacs': total_vacs,
                               'location': location, 'employee_count': employee_count,
                               'description': description,
                               'vacancies': co_vacancies, })


class VacancyView(View):
    def get(self, request, pk, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        if vacancy is None:
            raise Http404
        title = "Вакансия №: " + str(vacancy.id)

        company = Company.objects.filter(name=vacancy.company).last()
        company_id = company.id
        company_logo = company.logo
        company_name = company.name
        company_location = company.location
        company_employee_count = company.employee_count

        return render(request, 'web/vacancy.html',
                      context={'title': title,
                               'company_id' : company_id,
                               'company_logo': company_logo,
                               'company_name': company_name,
                               'company_location': company_location,
                               'company_employee_count': company_employee_count,
                               'vacancy': vacancy, })

class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all().order_by('-published_at')
        total_vacancies = vacancies.count()
        title = "Все вакансии"

        return render(request, 'web/vacancy.html',
                      context={'title': title,
                               'total_vacancies' : total_vacancies,
                               'vacancies': vacancies, })
