# Generated by Django 3.2.5 on 2021-08-02 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_department_department'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Department',
            new_name='Departments',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='department',
        ),
        migrations.AddField(
            model_name='customuser',
            name='departments',
            field=models.ManyToManyField(to='users.Departments'),
        ),
    ]
