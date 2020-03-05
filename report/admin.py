from django.contrib import admin
from .models import AllReportType, Reports

class ReportAdminb(admin.ModelAdmin):
        list_display = ('types_of_report','igihe_itangirwa','deadline','owner')

class ReportAdmin(admin.ModelAdmin):
        list_display = ('report_type','report_file','submitted_on',)

admin.site.register(Reports, ReportAdmin)

admin.site.register(AllReportType,ReportAdminb)
