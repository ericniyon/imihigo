from django import forms
from .models import *


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('time_of_report','report_name', 'report_file')
        widgets = {
            'report_file': forms.FileInput(attrs={'style': ' border-radius:2px;);'}),

        }
        labels={
            'report_name':'Raporo Itanzwe',
            'report_file':' Dosiye ya Raporo Itanzwe'
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields["report_name"].queryset = TypesOfReport.objects.filter(owner=self.request.user.user_profile)
        # self.fields['report_type'].help_text = "urugero: raporo y' imari ni igena migambi"
        # self.fields['report_file'].help_text = 'urugero:  file igaragaza raporo utanze '


