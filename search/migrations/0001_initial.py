# Generated by Django 2.1.5 on 2019-01-27 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent', models.DateTimeField()),
                ('nick', models.CharField(max_length=30)),
                ('recipient', models.CharField(max_length=30, null=True)),
                ('message', models.CharField(max_length=512)),
            ],
        ),
    ]
