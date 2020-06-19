from django.db import models

# Create your models here.


class News(models.Model):
    heading = models.CharField('Заголовок', max_length=100, blank=True)
    title = models.CharField('Название статьи', max_length=200)
    text = models.TextField('Текст')
    photo = models.ImageField('Картинка')
    pub_date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    def was_published_recently(self):  # надо не совсем
        pass

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
