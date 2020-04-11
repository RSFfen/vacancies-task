from django.contrib import admin

# Register your models here.

from .models import Vacancy
admin.site.register(Vacancy)

from .models import Company
admin.site.register(Company)

from .models import Specialty
admin.site.register(Specialty)
