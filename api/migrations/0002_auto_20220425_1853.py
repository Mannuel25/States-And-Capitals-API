# Generated by Django 3.0.1 on 2022-04-25 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='states',
            old_name='contributor_id',
            new_name='contributor',
        ),
    ]
