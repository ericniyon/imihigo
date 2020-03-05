from .models import Indicator,Item,Indicator_target,Raporo_yimihigo
from django import forms


class ImihigoForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ("sector","indicator","target","item","item_target","measurement")

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['indicator'].queryset = Indicator.objects.none()

        if 'sector' in self.data:
            try:
                sector_id = int(self.data.get('sector'))
                self.fields['indicator'].queryset = Indicator.objects.filter(sector_id=sector_id).order_by('indicator_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['indicator'].queryset = self.instance.sector.indcator_set.order_by('indicator_name')
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['target'].queryset = Indicator_target.objects.none()
        if 'indicator' in self.data:
            try:
                indcator_id = int(self.data.get('indicator'))
                self.fields['target'].queryset = Indicator_target.objects.filter(indcator_id=indcator_id).order_by('target_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['target'].queryset = self.instance.indcator.target_set.order_by('target_name')
        
            
    
class RaporoYimihigoForm(forms.ModelForm):
    
    class Meta:
        model = Raporo_yimihigo
        fields = ("report_quater","items_to_report_on","current_status","comments")


    

    
