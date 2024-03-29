# Generated by Django 2.0.7 on 2019-06-02 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0003_auto_20190602_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ques',
            name='asked',
        ),
        migrations.RemoveField(
            model_name='ques',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='ques',
            name='time_asked',
        ),
        migrations.AddField(
            model_name='ques',
            name='ques',
            field=models.CharField(default=None, max_length=150, unique=True),
        ),
        migrations.AddField(
            model_name='ques',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ques',
            name='id1',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ques',
            name='name',
            field=models.CharField(max_length=20, verbose_name="person's name"),
        ),
    ]
