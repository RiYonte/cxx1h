# Generated by Django 2.2 on 2019-04-26 18:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stdsys', '0002_remove_tags_tcolor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.CharField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='stdsys.Student')),
            ],
        ),
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]
