from django.db import models

class Prediction(models.Model):
    """Предсказания"""
    prediction = models.TextField(verbose_name='Предсказания')
