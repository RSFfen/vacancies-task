from django.db import models

# Create your models here.

class Vacancy(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Название:')
    specialty = models.ForeignKey('Specialty', on_delete = models.DO_NOTHING, null = True, blank = True, related_name="vacancies", verbose_name = 'Специализация:')
    company = models.ForeignKey('Company', on_delete = models.DO_NOTHING, null = True, blank = True, related_name="vacancies", verbose_name = 'Компания:')
    skills = models.TextField(max_length=50, null=True, blank=True, verbose_name='Навыки:')
    description = models.TextField(max_length=50, null=True, blank=True, verbose_name='Описание:')
    salary_min = models.IntegerField(null=True, blank=True, verbose_name='Зарплата от:')
    salary_max = models.IntegerField(null=True, blank=True, verbose_name='Зарплата до:')
    published_at = models.DateField(null=True, verbose_name='Опубликовано:')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Вакансии'
        verbose_name = 'Вакансия'
        ordering = ['-published_at', 'title']

class Company(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Название:')
    location = models.CharField(max_length=50, null=True, blank=True, verbose_name='Город:')
    logo = models.CharField(max_length=50, null=True, blank=True, verbose_name='Логотипчик:')
    description = models.TextField(max_length=50, null=True, blank=True, verbose_name='Информация о компании:')
    employee_count = models.IntegerField(null=True, blank=True, verbose_name='Количество сотрудников :')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Компании'
        verbose_name = 'Компания'
        ordering = ['name']

class Specialty(models.Model):
    code = models.CharField(max_length=10, null=True, blank=True, verbose_name='Код:')
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Название:')
    picture = models.CharField(max_length=50, null=True, blank=True, verbose_name='Картинка:')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = 'Специализации'
        verbose_name = 'Специализация'
        ordering = ['code']