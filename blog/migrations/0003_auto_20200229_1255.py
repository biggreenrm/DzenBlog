# Generated by Django 2.2.10 on 2020-02-29 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200229_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='theme',
            field=models.CharField(choices=[('th', 'Theory'), ('pr', 'Practice'), ('po', 'Poetry'), ('mf', 'Mindflow')], default='th', max_length=255),
        ),
    ]