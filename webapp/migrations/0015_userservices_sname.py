# Generated by Django 4.2 on 2023-10-05 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_alter_userservices_sdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userservices',
            name='Sname',
            field=models.CharField(max_length=67, null=True),
        ),
    ]