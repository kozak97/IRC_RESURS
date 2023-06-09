# Generated by Django 4.1.7 on 2023-04-13 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=700, verbose_name='Категорія')),
                ('slug', models.SlugField(max_length=700, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Катагорії',
                'verbose_name_plural': 'Катагорії',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=700, verbose_name='Зголовок')),
                ('slug', models.SlugField(max_length=700, unique=True, verbose_name='Slug')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('file', models.FileField(null=True, upload_to='files/%Y/%m/%d/', verbose_name='Файл')),
                ('link', models.URLField(null=True, verbose_name='Посилання')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Час створення')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Час коригування')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубліквано')),
            ],
            options={
                'verbose_name': 'Новини',
                'verbose_name_plural': 'Новини',
                'ordering': ['-time_create', '-title'],
            },
        ),
        migrations.CreateModel(
            name='ProIrc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=700, verbose_name='Зголовок')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('photo', models.ImageField(upload_to='photos_irc/%Y/%m/%d/', verbose_name='Фото')),
                ('link', models.URLField(null=True, verbose_name='Посилання')),
                ('contact', models.CharField(max_length=700, verbose_name='Контакти')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Про ІРЦ',
                'verbose_name_plural': 'Про ІРЦ',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=300, verbose_name='Призвіще')),
                ('last_name', models.CharField(db_index=True, max_length=200, verbose_name="Ім'я")),
                ('pobatkovi', models.CharField(db_index=True, max_length=400, verbose_name='По батькові')),
                ('birth_day', models.CharField(db_index=True, max_length=100, verbose_name='Дата народження')),
                ('posada', models.CharField(db_index=True, max_length=400, verbose_name='Посада')),
                ('info', models.CharField(db_index=True, max_length=8000, verbose_name='Інформація про себе')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictures', models.ImageField(null=True, upload_to='pictures/%Y/%m/%d/', verbose_name='Фотографії')),
                ('news', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='irc_news.news', verbose_name='Публікація')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Фотографії',
                'ordering': ['pictures'],
            },
        ),
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='irc_news.users'),
        ),
        migrations.AddField(
            model_name='news',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='irc_news.categorie'),
        ),
        migrations.CreateModel(
            name='Comentari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=700, verbose_name="Ім'я")),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('news', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='irc_news.news', verbose_name='Публікація')),
            ],
            options={
                'verbose_name': 'Коментарі',
                'verbose_name_plural': 'Коментарі',
                'ordering': ['-id'],
            },
        ),
    ]
