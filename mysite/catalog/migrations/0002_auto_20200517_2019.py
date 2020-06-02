# Generated by Django 3.0.5 on 2020-05-17 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='personid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='catalog.Person'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='HHHH', max_length=512),
        ),
    ]
