# Generated by Django 2.2 on 2019-04-26 09:49

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ITtestapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ittest',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='富文本'),
        ),
    ]
