# Generated by Django 2.2 on 2019-04-26 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stdsys', '0003_auto_20190427_0245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='tags',
            new_name='tag',
        ),
    ]
