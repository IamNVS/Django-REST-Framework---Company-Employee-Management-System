from django.contrib import admin
from api.models import Company,Employee
# Register your models here.

class Company_Admin(admin.ModelAdmin):
    list_display = ('company_id','company_name','company_location','company_about','type')
    search_fields = ('company_name',)

class Employee_Admin(admin.ModelAdmin):
    list_display = ('employee_id','employee_name','employee_email','employee_phone','employee_about','employee_position','company')
    search_fields = ('employee_name',)
    list_filter = ('company',)


admin.site.register(Company, Company_Admin)
admin.site.register(Employee, Employee_Admin)
