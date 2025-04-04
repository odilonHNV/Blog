# Generated by Django 5.1.5 on 2025-03-12 01:50

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0009_alter_article_image'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='Image/'),
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_com', models.CharField(max_length=200)),
                ('date_dreation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de création')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogApp.article', verbose_name='Article')),
                ('user_com', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userprofil', verbose_name='Auteur')),
            ],
        ),
    ]
