from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Service(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name=u'Название Услуги')
    text = RichTextUploadingField(blank=True, null=True, default=None, verbose_name=u'Текст к услуге')
    short_description = models.TextField(blank=True, null=True, default=None, verbose_name=u'Краткое содержание')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='Service_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография услуги'
        verbose_name_plural = 'Фотографии услуг'