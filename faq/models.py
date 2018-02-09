from django.db import models

class Faq(models.Model):
    class Meta():
        db_table = 'faq'
        verbose_name = u'Вопрос/ответ'
        verbose_name_plural = u'Вопросы/ответы'
    faq_title = models.CharField(max_length=60, verbose_name=u'Заголовок')
    faq_text = models.TextField(verbose_name=u'Текст')
    # about_image = models.ImageField(null=True, blank=True, upload_to="images/",
    #                                   verbose_name=u'Изображение', )

    def __str__(self):
        return self.faq_text[:50] + "..."