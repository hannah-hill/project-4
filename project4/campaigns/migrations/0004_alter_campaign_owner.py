# Generated by Django 3.2.9 on 2021-12-02 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campaigns', '0003_campaign_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
