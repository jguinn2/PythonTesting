# Generated by Django 2.2.1 on 2019-06-25 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_importance_knowledgearea_mymodelname_outcome_subknowledgearea_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='xml_output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_text', models.TextField(help_text='output file', max_length=10000)),
            ],
        ),
    ]