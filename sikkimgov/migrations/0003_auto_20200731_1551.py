# Generated by Django 3.0.8 on 2020-07-31 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikkimgov', '0002_auto_20200729_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiaries',
            name='phase1',
        ),
        migrations.RemoveField(
            model_name='beneficiaries',
            name='phase2',
        ),
        migrations.RemoveField(
            model_name='beneficiaries',
            name='phase3',
        ),
        migrations.RemoveField(
            model_name='beneficiaries',
            name='phase4',
        ),
        migrations.RemoveField(
            model_name='beneficiaries',
            name='phase5',
        ),
        migrations.RemoveField(
            model_name='beneficiaries',
            name='phase6',
        ),
        migrations.RemoveField(
            model_name='initial',
            name='intrmed_adhaar',
        ),
        migrations.AlterField(
            model_name='initial',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]