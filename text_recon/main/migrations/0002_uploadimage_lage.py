# Generated by Django 4.1 on 2022-09-01 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadimage',
            name='lage',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
