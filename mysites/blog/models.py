from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    class Status(models.TextChoices):  # Добавление поля статус
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')  # Добавление поля автора, связь с моделью User
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)  # Добавление поля статуса

    class Meta:
        ordering = ['-publish']  # Добавление отображения по убыванию жаты публикации
        indexes = [
            models.Index(fields=['-publish']),  # Добавление индексации для нового комита
        ]

    def __str__(self):
        return self.title
