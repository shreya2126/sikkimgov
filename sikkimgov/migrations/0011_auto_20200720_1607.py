# Generated by Django 2.2.3 on 2020-07-20 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikkimgov', '0010_auto_20200719_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intermediatorloginform',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
