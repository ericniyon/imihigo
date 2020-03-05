from django.urls import path
from .views import imihigo_view,Imihigo,load_indicators,load_target,raporoKumihigo




urlpatterns = [
    
    path('', imihigo_view, name='imihigo'),
    path('imihigo/' , Imihigo.as_view(), name='imihigo_yose'),
    path('ajax/load-indicators/', load_indicators, name='ajax_load_indicators'),
    path('ajax/load-targets/', load_target, name='ajax_load_targets'),
    path('raporo/', raporoKumihigo, name='guhigura'),


]
