# Generated by Django 5.1.5 on 2025-03-22 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0011_alter_commentaire_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
