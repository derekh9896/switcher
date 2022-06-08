# Generated by Django 4.0.5 on 2022-06-08 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_services_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing_info',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='website.users')),
                ('credit_num', models.CharField(max_length=16)),
                ('expiration', models.IntegerField()),
                ('cvc', models.IntegerField()),
                ('card_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='billing_info',
        ),
    ]