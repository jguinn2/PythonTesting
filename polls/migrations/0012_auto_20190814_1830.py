# Generated by Django 2.2.1 on 2019-08-14 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20190626_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hours_per_semester_f',
            name='hours_per_semester_text',
            field=models.CharField(max_length=200),
        ),
    ]
