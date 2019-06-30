# Generated by Django 2.2.2 on 2019-06-29 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter department name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter project name', max_length=100)),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Already Finished')),
                ('status', models.CharField(blank=True, choices=[('o', 'Ongoing'), ('c', 'Completed')], default='m', help_text='Project completion status', max_length=1)),
                ('description', models.CharField(help_text='Brief Description of project', max_length=1000)),
                ('srs_link', models.URLField(blank=True, help_text='Enter the URL to the SRS of this project', null=True)),
                ('project_link', models.URLField(blank=True, help_text='Enter the github link of your project', null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter technology used like web, machine learning, etc.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(help_text="Enter student's first name", max_length=50)),
                ('lName', models.CharField(help_text="Enter student's last name", max_length=50)),
                ('school', models.CharField(help_text='Enter the name of your school', max_length=100)),
                ('email', models.EmailField(help_text='Enter your email', max_length=254)),
                ('github', models.URLField(blank=True, help_text='Enter your github link', null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Department')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tech_used',
            field=models.ManyToManyField(help_text='Tech Used in project', null=True, to='catalog.Technology'),
        ),
    ]