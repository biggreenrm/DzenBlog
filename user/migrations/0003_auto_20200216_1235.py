# Generated by Django 2.2.10 on 2020-02-16 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='sex',
            field=models.CharField(choices=[('man', 'Мужчина'), ('woman', 'Женщина'), ('secret', 'Скрыт')], default='Скрыт', max_length=2),
        ),
    ]
