# Generated by Django 5.1.5 on 2025-03-27 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0013_rename_date_dreation_commentaire_date_reaction_and_more'),
        ('user', '0002_alter_userprofil_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='user_com',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_com', to='user.userprofil', verbose_name='Auteur'),
        ),
    ]
