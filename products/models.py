from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name=u'Название продукции')
    text = RichTextUploadingField(blank=True, null=True, default=None, verbose_name=u'Текст к продукции')
    short_description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукции'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'