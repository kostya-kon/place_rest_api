from django.db import models

# Create your models here.


class Author(models.Model):
    """Модель Автора, который будет оставлять заметки"""
    nickname = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        """Удобное утображение модели"""
        return self.nickname


class Notice(models.Model):
    """Модель заметки про место"""
    title = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    description = models.TextField()
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        """Удобное утображение модели"""
        return self.title