# Generated by Django 3.2.4 on 2021-06-12 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_pessoa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pessoa',
        ),
    ]
