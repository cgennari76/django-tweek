# Generated by Django 3.2.13 on 2022-04-23 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=150)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
