# Generated by Django 3.0.7 on 2020-06-19 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50, verbose_name='Срочно')),
            ],
        ),
    ]
