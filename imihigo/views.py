from django.shortcuts import render
from .forms import ImihigoForm,RaporoYimihigoForm
from django.views.generic import ListView
from .models import Indicator,Item,Raporo_yimihigo,Indicator_target
from django.db.models import Sum


def imihigo_view(request):

    imihigo_form = ImihigoForm(request.POST or None)
    if imihigo_form.is_valid():
        imihigo_form.save()

        imihigo_form = ImihigoForm()
        
    template_name = 'imihigo/imihigo_new.html'
    context={'imihigo_form':imihigo_form}

    return render(request,template_name, context)

def load_indicators(request):
    sector_id = request.GET.get('sector')
    indicators = Indicator.objects.filter(sector_id=sector_id).order_by('indicator_name')
    return render(request, 'imihigo/options.html', {'indicators': indicators})

def load_target(request):
    indicator_id = request.GET.get('indicator')
    targets = Indicator_target.objects.filter(indicator_id=indicator_id).order_by('target_name')

    return render(request, 'imihigo/options.html', {'targets': targets})





class Imihigo(ListView):
    
    model = Raporo_yimihigo
    template_name = 'imihigo/imihigo_yakozwe.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reports"] = Raporo_yimihigo.objects.all().order_by('items_to_report_on')
        indicator=Indicator_target.objects.all()
        context["items"] =Item.objects.filter(indicator=1)
        context['sum1']=Raporo_yimihigo.objects.values('items_to_report_on__item_target').annotate(Sum('items_to_report_on__item_target'))
        # context['total_paid']= Raporo_yimihigo.objects.all().annotate(Sum('items_to_report_on__item_target'))['items_to_report_on__item_target__sum']

        


        return context
    

def raporoKumihigo(request):
    template_name = 'imihigo/option2.html'

    raporo = RaporoYimihigoForm(request.POST or None)
    if raporo.is_valid():
        raporo.save()

        raporo = RaporoYimihigoForm()

    context={
        'raporo':raporo
    }
    return render(request, template_name, context)
