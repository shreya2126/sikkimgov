# Generated by Django 3.0.8 on 2020-08-02 11:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sikkimgov', '0002_remove_intermediatorloginform_adhaarimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intermediatorloginform',
            name='dateofbirth',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]