# Generated by Django 3.2 on 2023-04-29 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('pending', 'Open'), ('close', 'Close')], default='open', max_length=10),
        ),
    ]