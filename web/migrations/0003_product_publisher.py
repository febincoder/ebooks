# Generated by Django 4.2.1 on 2023-05-20 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_product_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publisher',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
