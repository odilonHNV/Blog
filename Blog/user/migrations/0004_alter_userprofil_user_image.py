# Generated by Django 5.1.5 on 2025-03-27 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_userprofil_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofil',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='Image/'),
        ),
    ]
