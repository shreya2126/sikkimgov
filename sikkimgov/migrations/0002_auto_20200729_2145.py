# Generated by Django 3.0.8 on 2020-07-29 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikkimgov', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='initial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intrmed_adhaar', models.IntegerField(blank=True, null=True)),
                ('img', models.ImageField(upload_to='initial/')),
            ],
        ),
        migrations.AddField(
            model_name='beneficiaries',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True),
        ),
        migrations.AddField(
            model_name='beneficiaries',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True),
        ),
        migrations.AddField(
            model_name='beneficiaries',
            name='phase1',
            field=models.ImageField(blank=True, null=True, upload_to='phase1'),
        ),
        migrations.AddField(
            model_name='beneficiaries',
            name='phase2',
            field=models.ImageField(blank=True, null=True, upload_to='phase2'),
        ),
        migrations.AddField(
            model_name='beneficiaries',
            name='phase3',
            field=models.ImageField(blank=True, null=True, upload_to='phase3'),
        ),
        migrations.AddField(
            model_name='beneficiaries',
            name='phase4',
            field=models.ImageField(blank=True, null=True, upload_to='phase4'),
        ),
        migrations.AddField(
            model_name='beneficiaries',
            name='phase5',
            field=models.ImageField(blank=True, null=True, upload_to='phase5'),
        ),
        migrations.AddField(
            model_name='beneficiaries',
            name='phase6',
            field=models.ImageField(blank=True, null=True, upload_to='phase6'),
        ),
    ]