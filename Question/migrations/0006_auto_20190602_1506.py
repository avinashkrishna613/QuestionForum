# Generated by Django 2.0.7 on 2019-06-02 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0005_auto_20190602_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ques',
            old_name='id',
            new_name='var',
        ),
    ]
