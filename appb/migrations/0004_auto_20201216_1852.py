# Generated by Django 3.0.8 on 2020-12-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appb', '0003_auto_20201129_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='costumer',
            name='nomorhp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]