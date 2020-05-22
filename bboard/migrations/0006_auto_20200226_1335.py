# Generated by Django 3.0.3 on 2020-02-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0005_remove_bb_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='image',
            field=models.ImageField(blank=True, upload_to='products', verbose_name='Изображения'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=100),
        ),
    ]