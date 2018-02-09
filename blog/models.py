from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    article_title = models.CharField(max_length=60, verbose_name='Заголовок')
    article_text = RichTextUploadingField(verbose_name='Текст статьи')
    short_text = models.TextField(null=True, blank=True, verbose_name='Краткое описание')
    article_date = models.DateTimeField(verbose_name="Дата и время")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.article_title
    class Meta():
        db_table = "blog"
        verbose_name = 'статьи'
        verbose_name_plural = 'статьи'
        ordering = ['-article_date']

class BlogImages(models.Model):
    class Meta():
        db_table = 'blog_images'
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    article = models.ForeignKey(Blog, null=True, blank=True, default=None)
    image = models.ImageField(null=True, blank=True, upload_to="images/blog/",
                                       verbose_name=u'Изображение', )
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.id