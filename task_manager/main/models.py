from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    status = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Purpose(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    rank = models.CharField(max_length=2)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'