# Generated by Django 3.0.8 on 2020-08-01 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='beneficiaries',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('phoneno', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('adhaarno', models.IntegerField(unique=True)),
                ('bankname', models.CharField(max_length=50)),
                ('accountno', models.IntegerField()),
                ('IFSC', models.CharField(max_length=50)),
                ('areafland', models.IntegerField()),
                ('adhaarimage', models.ImageField(blank=True, null=True, upload_to='adhaarimage')),
                ('registryimage', models.ImageField(blank=True, null=True, upload_to='registryimage')),
                ('latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('otp', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('level', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='initial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='initial/')),
                ('beni_adhar', models.IntegerField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='intermediatorLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intermediatorid', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Intermediatorloginform',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('fathername', models.CharField(max_length=20)),
                ('contactno', models.IntegerField()),
                ('alternatecontactno', models.IntegerField()),
                ('adhaarno', models.IntegerField(unique=True)),
                ('email', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=200)),
                ('district', models.CharField(blank=True, max_length=200, null=True)),
                ('region', models.CharField(max_length=200)),
                ('dateofbirth', models.DateField(blank=True, null=True)),
                ('adhaarimage', models.ImageField(blank=True, null=True, upload_to='adhaarimage')),
            ],
        ),
    ]
