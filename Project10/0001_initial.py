# Generated by Django 2.2 on 2019-04-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('fee', models.DecimalField(decimal_places=3, max_digits=20)),
            ],
        ),
    ]
