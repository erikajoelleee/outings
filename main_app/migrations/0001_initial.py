# Generated by Django 4.2.4 on 2023-08-11 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('sport', models.CharField(choices=[('F', 'Football'), ('B', 'Basketball'), ('B', 'Baseball')], default='F', max_length=1)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
