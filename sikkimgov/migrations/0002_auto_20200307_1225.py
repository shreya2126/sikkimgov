# Generated by Django 2.2.3 on 2020-03-07 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikkimgov', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiaries',
            name='adhaarno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='beneficiaries',
            name='phoneno',
            field=models.IntegerField(),
        ),
    ]
