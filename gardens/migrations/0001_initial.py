# Generated by Django 3.2.18 on 2023-05-25 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields
import gardens.models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Content')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('category', models.CharField(choices=[('전체', '전체'), ('식물원', '식물원'), ('전시회', '전시회'), ('정원 센터', '정원 센터'), ('이벤트', '이벤트')], max_length=20)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=gardens.models.Garden.garden_images_path)),
                ('site_link', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('like_user', models.ManyToManyField(related_name='like_gradens', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=gardens.models.Comment.garden_images_path)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='gardens.garden')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
