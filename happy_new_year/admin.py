from django.contrib import admin

from .models import Message, Prediction


class MessageAdmin(admin.ModelAdmin):
    """Регистрация таблицы рассылок в админке"""
    list_display = [field.name for field in Message._meta.fields]  # Модель в виде таблицы


admin.site.register(Message, MessageAdmin)  # Регистрируем модель в админке


class PredictionAdmin(admin.ModelAdmin):
    """Регистрация таблицы рассылок в админке"""
    list_display = [field.name for field in Prediction._meta.fields]  # Модель в виде таблицы


admin.site.register(Prediction, PredictionAdmin)  # Регистрируем модель в админке
