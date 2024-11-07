# Generated by Django 5.1.1 on 2024-11-07 03:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnSapModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('gate_pass_no', models.CharField(max_length=10)),
                ('billing_doc_no', models.CharField(max_length=10)),
                ('billing_date', models.DateField()),
                ('route', models.CharField(max_length=10)),
                ('return_type', models.CharField(choices=[('p', 'p'), ('f', 'f')], max_length=10)),
                ('return_reason', models.CharField(choices=[(901, 'Wrong Order'), (902, 'Pharmacy Closed'), (903, 'Customer Denied to Accept'), (904, 'No Order'), (905, 'Cash Short'), (906, 'Delayed Delivery'), (907, 'Damaged Goods'), (908, 'Price Difference'), (909, 'Quantity Discrepancy'), (910, 'Discount Discrepancy'), (911, 'Order Mistakenly Created'), (912, 'Out of Schedule'), (913, 'Route Cancelled'), (914, 'Natural Disaster'), (915, 'Short Dated Material'), (916, 'Rate Increase'), (917, 'Patient No More Alive'), (918, 'Mistakenly Created By Depot'), (919, 'PQC')], max_length=10)),
            ],
            options={
                'verbose_name': 'SAP Return',
                'verbose_name_plural': 'SAP Return',
                'db_table': 'rdl_return_sap',
            },
        ),
        migrations.CreateModel(
            name='ReturnListSAPModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('matnr', models.CharField(max_length=10)),
                ('batch', models.CharField(max_length=10)),
                ('return_quantity', models.IntegerField()),
                ('sales_quantity', models.IntegerField()),
                ('return_no', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sap_app.returnsapmodel')),
            ],
            options={
                'verbose_name': 'SAP Return List',
                'verbose_name_plural': 'SAP Return List',
                'db_table': 'rdl_return_list_sap',
            },
        ),
    ]
