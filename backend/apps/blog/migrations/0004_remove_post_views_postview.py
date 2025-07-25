# Generated by Django 4.2.23 on 2025-07-22 15:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
        migrations.CreateModel(
            name='PostView',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ip_address', models.GenericIPAddressField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post_view', to='blog.post')),
            ],
            options={
                'verbose_name': 'Post View',
                'verbose_name_plural': 'Post Views',
                'ordering': ['-timestamp'],
            },
        ),
    ]
