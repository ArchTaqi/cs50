# Generated by Django 2.0.3 on 2018-03-29 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20180329_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passanger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passanger', to='flights.Flight')),
            ],
        ),
        migrations.AlterField(
            model_name='airport',
            name='code',
            field=models.CharField(max_length=5),
        ),
    ]