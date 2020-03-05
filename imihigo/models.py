from django.db import models
from django.utils import timezone

PILLARS=[
    ('ECONOMIC TRANSFORMATION PILLAR ','ECONOMIC TRANSFORMATION PILLAR '),
    ('SOCIAL  TRANSFORMATION PILLAR','SOCIAL  TRANSFORMATION PILLAR'),
    ('TRANSFORMATIONAL GOVERNANCE','TRANSFORMATIONAL GOVERNANCE'),
]

class Pillsector(models.Model):
    pillar = models.CharField(max_length=80,choices=PILLARS)
    sector =models.CharField(max_length=250)

    def __str__(self):
        return self.sector

class Indicator(models.Model):
    indicator_name = models.CharField(max_length=200)
    sector = models.ForeignKey(Pillsector,on_delete=models.CASCADE)
    time = models.DateField(default=timezone.now())

    def __str__(self):
        return self.indicator_name



TARGET_FORMATION=[
    ('Numbers','Numbers'),
    ('Percentage','Percentage'),
]



class Indicator_target(models.Model):
    target_name=models.CharField(max_length=100)
    indicator=models.ForeignKey(Indicator,on_delete=models.CASCADE)
    target_type = models.CharField(choices=TARGET_FORMATION,max_length=50, default='Numbers')

    def __str__(self):
        return self.target_name

class Unit(models.Model):
    unit_type = models.CharField(max_length=10)

    def __str__(self):
        return self.unit_type


class Item(models.Model):
    sector=models.ForeignKey(Pillsector, on_delete=models.CASCADE)
    indicator=models.ForeignKey(Indicator,on_delete=models.CASCADE)
    target=models.ForeignKey(Indicator_target,on_delete=models.CASCADE)
    item=models.CharField(max_length=50,help_text='Example  Banana .. etc')
    item_target=models.PositiveIntegerField(help_text='Example   120,900  ect')
    measurement = models.ForeignKey(Unit, on_delete=models.CASCADE,blank=True,default=1)



    def __str__(self):
        return self.item

IBIHEMBWE=[
    ('Q1','Quater 1'),
    ('Q2','Quater 2'),
    ('Q3','Quater 3'),
    ('Q4','Quater 4'),

]


class Raporo_yimihigo(models.Model):
    report_quater = models.CharField(max_length=50, choices=IBIHEMBWE)
    items_to_report_on = models.ForeignKey(Item,on_delete=models.CASCADE)
    current_status = models.PositiveIntegerField()
    comments = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.report_quater

    



