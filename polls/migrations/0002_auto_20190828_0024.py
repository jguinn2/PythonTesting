# Generated by Django 2.2.1 on 2019-08-28 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses_f',
            old_name='workload_hours',
            new_name='workloadhours',
        ),
    ]
