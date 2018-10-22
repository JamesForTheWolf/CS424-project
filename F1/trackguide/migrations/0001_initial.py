# Generated by Django 2.1.2 on 2018-10-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_name', models.CharField(max_length=100)),
                ('track_length', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]