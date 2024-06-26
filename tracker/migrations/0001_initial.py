import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('e_mail', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
                ('Image', models.ImageField(upload_to='static/profile/')),
                ('address', models.CharField(max_length=128)),
                ('birth_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('ID', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('Image', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.user')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('inout', models.BooleanField(null=True, verbose_name='inout')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.user')),
            ],
        ),
    ]
