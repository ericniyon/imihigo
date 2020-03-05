from django.contrib import admin

from .models import*

class ItemDisplay(admin.ModelAdmin):
    target=models.ForeignKey(Indicator_target,on_delete=models.CASCADE)
    list_display=('sector','indicator','target','item','item_target')
    list_filter = ('indicator',)
    search_fields=('sector',)

class RaporoAdmin(admin.ModelAdmin):
    list_filter = ('items_to_report_on',)
    search_fields=('items_to_report_on',)
    


class TargetAdmin(admin.ModelAdmin):
    search_fields=('target_name',)


class IndicatorAdmin(admin.ModelAdmin):
    search_fields=('sector',)
    list_display=('indicator_name','sector','time')
    list_filter=('time',)


admin.site.register(Pillsector)
admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(Indicator_target,TargetAdmin)

admin.site.register(Item,ItemDisplay)
admin.site.register(Raporo_yimihigo, RaporoAdmin)
admin.site.register(Unit)

