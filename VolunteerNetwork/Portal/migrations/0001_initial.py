# Generated by Django 2.2 on 2020-05-17 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=100)),
                ('oauth_code', models.CharField(max_length=100)),
            ],
        ),
    ]
