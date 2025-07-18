# Generated by Django 4.2.23 on 2025-07-17 04:35

import apps.blog.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=apps.blog.models.category_thumbnail_directory)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=256)),
                ('content', models.TextField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=apps.blog.models.blog_thumbnail_directory)),
                ('keywords', models.CharField(blank=True, max_length=128)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.category')),
            ],
            options={
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'Blog Posts',
                'ordering': ('status', '-created_at'),
            },
        ),
        migrations.CreateModel(
            name='Heading',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=256)),
                ('slug', models.SlugField(max_length=256, unique=True)),
                ('level', models.PositiveIntegerField(choices=[(1, 'H1'), (2, 'H2'), (3, 'H3'), (4, 'H4'), (5, 'H5'), (6, 'H6')])),
                ('order', models.PositiveIntegerField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='headings', to='blog.post')),
            ],
            options={
                'verbose_name': 'Heading',
                'verbose_name_plural': 'Headings',
                'ordering': ['order'],
            },
        ),
    ]
