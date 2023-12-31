# Generated by Django 2.2.3 on 2023-09-13 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing_profiles', '0002_auto_20230912_1449'),
        ('orders', '0004_order_promo_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing_profiles.BillingProfile'),
        ),
    ]
