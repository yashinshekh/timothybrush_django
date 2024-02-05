# Generated by Django 4.2.6 on 2024-02-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0003_product_category_product_color_product_size"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female"), ("other", "Other")], default="other", max_length=10
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[("tshirt", "T-shirts"), ("cap", "Baseball Caps"), ("toque", "Toques")],
                default="tshirt",
                max_length=10,
            ),
        ),
    ]
