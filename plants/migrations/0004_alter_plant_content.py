# Generated by Django 3.2.18 on 2023-06-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_alter_plant_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='content',
            field=models.CharField(max_length=460),
        ),
    ]