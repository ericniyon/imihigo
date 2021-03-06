# Generated by Django 3.0.2 on 2020-03-01 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllReportType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types_of_report', models.CharField(max_length=300)),
                ('igihe_itangirwa', models.PositiveSmallIntegerField(choices=[(1, 'Icyumweru'), (2, 'Ukwezi'), (3, 'Igihembwe'), (4, 'Amezi atandatu'), (5, 'Umwaka')], help_text='eg: Icyumweru, Ukwezi etc..')),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Department')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_file', models.FileField(upload_to='reports')),
                ('submitted_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('report_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.AllReportType')),
            ],
        ),
    ]
