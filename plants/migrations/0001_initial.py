# Generated by Django 3.2.18 on 2023-06-11 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import plants.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=460)),
                ('allergy', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('watering', models.CharField(max_length=20)),
                ('sunlight', models.CharField(max_length=20)),
                ('humidity', models.CharField(max_length=20)),
                ('temperature', models.CharField(max_length=20)),
                ('like_users', models.ManyToManyField(related_name='like_plants', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlantImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(default=plants.models.PlantImage.default_image, upload_to='plants/images')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plant_images', to='plants.plant')),
            ],
        ),
    ]
