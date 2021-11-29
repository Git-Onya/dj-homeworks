from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    name = models.CharField(max_length=256, verbose_name='Раздел')
    articles = models.ManyToManyField(Article, related_name='scopes', through='Tag')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='tags')
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, related_name='tags')
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        unique_together = [['article', 'scope']]
