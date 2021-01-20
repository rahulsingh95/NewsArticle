# Generated by Django 3.1.5 on 2021-01-20 19:59

import blog.managers
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('street', models.CharField(blank=True, max_length=255)),
                ('zip', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Category Id', primary_key=True, serialize=False)),
                ('title', models.CharField(default='', help_text='Category Title', max_length=24)),
                ('description', models.CharField(help_text='Category Description', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(help_text='User Email', max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, help_text=' User First Name', max_length=255)),
                ('last_name', models.CharField(blank=True, help_text='User Last Name', max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('U', 'Unknown')], default='U', help_text='Gender choice M, F, O, U', max_length=16)),
                ('birth_date', models.DateField(help_text=' Date of birth of user', null=True)),
                ('contact_address', models.OneToOneField(blank=True, default=None, help_text='User Contact address related to address class ', null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.address')),
            ],
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('headline', models.CharField(help_text='News article headline', max_length=200, unique=True)),
                ('content', models.TextField(help_text='News content')),
                ('published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(help_text='News authored by user', on_delete=django.db.models.deletion.CASCADE, related_name='news_article_post', related_query_name='news_article_posts', to='blog.user')),
                ('category', models.ForeignKey(help_text='News category', on_delete=django.db.models.deletion.CASCADE, related_name='article_category', related_query_name='article_categories', to='blog.category')),
            ],
        ),
    ]
