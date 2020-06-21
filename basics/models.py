from django.db import models

# Create your models here.


class News(models.Model):
    heading = models.CharField('Заголовок', max_length=100, blank=True)
    title = models.CharField('Название статьи', max_length=200)
    text = models.TextField('Текст')
    photo = models.ImageField('Картинка')  # Пока не мигровали
    pub_date = models.DateField('Дата публикации')
    sep_page = models.BooleanField('Нужна ли отдельная ссылка')  # Откывать ли на отдельной странице

    def __str__(self):
        return self.title

    def was_published_recently(self):  # надо не совсем
        pass

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Urgent(models.Model):
    text = models.CharField('Срочно', max_length=50)
    link = models.CharField('Ссылка', max_length=20, default=None)

    def __str__(self):
        return self.text
