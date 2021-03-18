# Generated by Django 3.1.7 on 2021-03-17 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('dept_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'departments',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SupportContacts',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(blank=True, max_length=32, null=True)),
                ('first_name', models.CharField(blank=True, max_length=32, null=True)),
                ('last_name', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.CharField(blank=True, max_length=64, null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.departments')),
            ],
            options={
                'db_table': 'support_contacts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SupportRequests',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('email', models.CharField(blank=True, max_length=64, null=True)),
                ('subject', models.CharField(blank=True, max_length=64, null=True)),
                ('message', models.CharField(blank=True, max_length=1500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.supportcontacts')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.departments')),
            ],
            options={
                'db_table': 'support_requests',
                'managed': True,
            },
        ),
    ]
