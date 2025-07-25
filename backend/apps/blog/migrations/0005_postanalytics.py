# Generated by Django 4.2.23 on 2025-07-22 17:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_views_postview'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostAnalytics',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('views', models.PositiveIntegerField(default=0)),
                ('impressions', models.PositiveIntegerField(default=0)),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('click_through_rate', models.FloatField(default=0.0)),
                ('avg_time_on_page', models.FloatField(default=0.0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post_analytics', to='blog.post')),
            ],
        ),
    ]
