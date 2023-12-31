# Generated by Django 4.2.7 on 2023-12-10 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_record_email_alter_record_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='address',
        ),
        migrations.RemoveField(
            model_name='record',
            name='city',
        ),
        migrations.RemoveField(
            model_name='record',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='record',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='record',
            name='state',
        ),
        migrations.RemoveField(
            model_name='record',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='record',
            name='notes',
            field=models.CharField(default='Some notes', max_length=500),
        ),
        migrations.AlterField(
            model_name='record',
            name='email',
            field=models.EmailField(default='some email', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='first_name',
            field=models.CharField(default='some name', max_length=50, unique=True),
        ),
    ]
