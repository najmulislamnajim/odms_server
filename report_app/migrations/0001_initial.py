# Generated by Django 4.2 on 2023-06-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReportOneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_delivary', models.TextField(blank=True)),
                ('total_delivary_done', models.TextField(blank=True)),
                ('total_cash', models.TextField(blank=True)),
                ('total_cash_done', models.TextField(blank=True)),
            ],
            options={
                'managed': False,
            },
        ),
    ]
