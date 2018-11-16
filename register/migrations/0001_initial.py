# Generated by Django 2.1 on 2018-10-10 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('legal', models.IntegerField(default=0)),
                ('code', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(auto_created=True, default='2018-10-10')),
                ('givenname', models.CharField(default='', max_length=32)),
                ('familyname', models.CharField(default='', max_length=32)),
                ('emailadd', models.EmailField(max_length=254, unique=True)),
                ('job', models.CharField(default='', max_length=255)),
                ('mobilenum', models.IntegerField(default=123456)),
                ('gender', models.CharField(choices=[('male', 'man'), ('female', 'woman')], default='male', max_length=32)),
                ('Uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.UserD', unique=True)),
            ],
        ),
    ]