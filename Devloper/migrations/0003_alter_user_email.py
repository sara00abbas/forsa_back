# Generated by Django 5.1.3 on 2025-02-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devloper', '0002_user_username_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
