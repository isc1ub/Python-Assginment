# Generated by Django 5.0.6 on 2024-05-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(choices=[('manager', 'Loyiha Menejeri'), ('hr_manager', 'HR Menejer'), ('backend_dev', 'Backend dasturchi'), ('seller', 'Sotuvchi'), ('frontend_dev', 'Frontend dasturchi'), ('devops', 'DevOps Injiner')], max_length=50),
        ),
    ]
