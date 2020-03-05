from django.shortcuts import render,redirect
from .forms import ReportForm

from .models import TypesOfReport,Report


def generate_report(request):
    report_form = ReportForm(request.POST, request.FILES,request=request)

    report_form.fields['report_name'].queryset = TypesOfReport.objects.filter(owner=1)

    if report_form.is_valid():
        report_form.save()
        # return redirect('dashboard')
        
        
    else:
        report_form = ReportForm(request=request)
     
    template_name = 'report/create_report.html'
    context       =  {'form':report_form}
    
    return render(request, template_name, context)


def created_report(request):
    reports = Report.objects.all()
    template = 'report/all_reports.html'
    context={
        'reports':reports
    }
    return render(request, template, context)