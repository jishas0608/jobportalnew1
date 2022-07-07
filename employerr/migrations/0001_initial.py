# Generated by Django 4.0.5 on 2022-06-21 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=120)),
                ('salary', models.PositiveIntegerField(null=True)),
                ('experience', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('last_date', models.DateField(null=True)),
                ('active_status', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=120)),
                ('logo', models.ImageField(null=True, upload_to='companyprofile')),
                ('location', models.CharField(max_length=120)),
                ('services', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employer12', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
