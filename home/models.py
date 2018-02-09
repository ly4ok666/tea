from django.db import models
# модель для создания статей, можно добавить что угодно для отображения
class Home(models.Model):
    # Заголовок статьи
    home_title = models.CharField(max_length=60, verbose_name='Заголовок')
    # Сам текст статьи
    home_text = models.TextField(verbose_name='Текст статьи')

    # Отображения статьи для разработчика и простоты поиска
    def __str__(self):
        return self.home_title

class HomeImage(models.Model):
    home = models.ForeignKey(Home, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='Home_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Картинки для слайдера'
        verbose_name_plural = 'Картинка для слайдера'