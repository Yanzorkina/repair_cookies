# Generated by Django 4.2.3 on 2023-07-30 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_order_model_alter_client_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount_due_by',
            field=models.FloatField(default=0, verbose_name='Сумма к оплате'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_completed',
            field=models.BooleanField(default=False, verbose_name='Оплала произведена?'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
    ]