# Generated by Django 2.2.2 on 2019-07-01 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20190630_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='disp_pic',
            field=models.ImageField(null=True, upload_to='static/users/'),
        ),
        migrations.AddField(
            model_name='student',
            name='disp_pic',
            field=models.ImageField(null=True, upload_to='static/users/'),
        ),
    ]
