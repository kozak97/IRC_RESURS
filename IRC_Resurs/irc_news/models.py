from django.conf import settings
from django.db import models
from django.utils.text import slugify
# Create your models here.
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=700, verbose_name='Зголовок')
    slug = models.SlugField(max_length=700, unique=True, db_index=True, verbose_name='Slug', )
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото', blank=False)

    file = models.FileField(upload_to="files/%Y/%m/%d/", verbose_name='Файл', blank=False, null=True)
    link=models.URLField(verbose_name='Посилання', blank=False, null=True)

    time_create=models.DateTimeField(auto_now_add=True, verbose_name='Час створення')
    time_update=models.DateTimeField(auto_now=True, verbose_name='Час коригування')
    is_published=models.BooleanField(default=True, verbose_name='Опубліквано')
    categorie = models.ForeignKey('Categorie', on_delete=models.PROTECT)
    author = models.ForeignKey('Users', on_delete=models.CASCADE, blank=False, null=True)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  reverse('one_page', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name='Новини'
        verbose_name_plural='Новини'
        ordering= ['-time_create', '-title']

class Pictures(models.Model):
    pictures = models.ImageField(upload_to="pictures/%Y/%m/%d/", verbose_name='Фотографії', null=True)
    news = models.ForeignKey('News', on_delete=models.CASCADE, verbose_name='Публікація', null=True)

    # def __str__(self):
    #     return self.news
    def get_absolute_url(self):
        return  reverse('delete_albom_one', kwargs={'id': self.pk})

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Фотографії'
        ordering = [ 'pictures' ]

class Categorie(models.Model):
    name = models.CharField(max_length=700, db_index=True, verbose_name='Категорія')
    slug = models.SlugField(max_length=700, unique=True, db_index=True, verbose_name='URL', )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Катагорії'
        verbose_name_plural='Катагорії'
        ordering= ['-id']

class Comentari(models.Model):
    name = models.CharField(max_length=700, verbose_name="Ім'я")
    content = models.TextField(blank=True, verbose_name='Контент')
    news = models.ForeignKey('News', on_delete=models.CASCADE, verbose_name='Публікація', null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Коментарі'
        verbose_name_plural='Коментарі'
        ordering= ['-id']


class ProIrc(models.Model):
    title = models.CharField(max_length=700, verbose_name='Зголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to="photos_irc/%Y/%m/%d/", verbose_name='Фото', blank=False)
    link=models.URLField(verbose_name='Посилання', blank=False, null=True)
    contact = models.CharField(max_length=700, verbose_name='Контакти')
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Про ІРЦ'
        verbose_name_plural='Про ІРЦ'


class Users(models.Model):
    first_name = models.CharField(max_length=300, db_index=True, verbose_name="Призвіще")
    last_name = models.CharField(max_length=200, db_index=True, verbose_name="Ім'я")
    pobatkovi = models.CharField(max_length=400, db_index=True, verbose_name="По батькові")
    birth_day = models.CharField(max_length=100, db_index=True, verbose_name="Дата народження")
    posada =  models.CharField(max_length=400, db_index=True, verbose_name="Посада")
    info =  models.CharField(max_length=8000, db_index=True, verbose_name="Інформація про себе")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Користувач', blank=False)

    def __str__(self):
        return self.first_name +' '+ self.last_name




