# Generated by Django 3.0.8 on 2022-04-30 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tbl_customers',
            },
        ),
    ]
