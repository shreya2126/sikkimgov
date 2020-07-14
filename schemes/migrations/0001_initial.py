# Generated by Django 3.0.8 on 2020-07-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=5000)),
                ('Description', models.CharField(max_length=50000)),
                ('Requirement', models.CharField(max_length=50000)),
                ('Pic', models.ImageField(upload_to='images')),
            ],
        ),
    ]
