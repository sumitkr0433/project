# Generated by Django 2.0.1 on 2020-03-01 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clustering',
            old_name='Algorithm',
            new_name='algorithm',
        ),
        migrations.RenameField(
            model_name='clustering',
            old_name='Intializer',
            new_name='intializer',
        ),
        migrations.RenameField(
            model_name='clustering',
            old_name='Max_iteration',
            new_name='max_iteration',
        ),
        migrations.RenameField(
            model_name='clustering',
            old_name='Number_of_chusks',
            new_name='number_of_chusks',
        ),
    ]
