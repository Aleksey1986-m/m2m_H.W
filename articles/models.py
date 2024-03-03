from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
        ordering = ['title']

    def __str__(self):
        return self.title


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Category, through='Scope', through_fields=('article', 'category'))


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='scopes')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='scopes', verbose_name='Категория')
    is_active = models.BooleanField()


    class Meta:
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'
        ordering = ['-is_active', 'category']