# Generated by Django 4.2.2 on 2023-07-21 17:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_order_repair_lvl"),
    ]

    operations = [
        migrations.AlterField(
            model_name="price",
            name="repair_lvl",
            field=models.IntegerField(
                choices=[
                    (1, "внешний осмотр, диагностика"),
                    (2, "Ремонт с разбором телефона, замена не паяных деталей"),
                    (3, "Замена дисплея, тачскрина"),
                    (4, "Электро-механический ремонт"),
                ],
                default=1,
                verbose_name="Уровень ремонта",
            ),
        ),
    ]