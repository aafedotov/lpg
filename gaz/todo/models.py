from django.db import models

from django.contrib.auth import get_user_model
from django.template.defaultfilters import truncatechars

User = get_user_model()


class Category(models.Model):

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Task(models.Model):

    category = models.ForeignKey(
        Category,
        related_name='tasks',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        help_text='Выберите категорию'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True
    )
    text = models.TextField(
        max_length=300,
        verbose_name='Текст задачи',
        help_text='Введите текст задачи'
    )

    @property
    def short_text(self):
        return truncatechars(self.text, 50)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text[:15]
