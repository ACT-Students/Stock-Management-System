# Generated by Django 3.0.7 on 2022-08-23 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20220823_1010'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorys',
            new_name='Category',
        ),
    ]
