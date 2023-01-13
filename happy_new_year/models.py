from django.db import models
from django.utils import timezone

import uuid


class Prediction(models.Model):
    """Предсказания"""
    prediction = models.TextField(verbose_name='Предсказания')


class Message(models.Model):
    """Сообщения"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.TextField(verbose_name='Сообщение')
    date_create = models.DateTimeField(default=timezone.now, blank=False, verbose_name='Дата создания')
