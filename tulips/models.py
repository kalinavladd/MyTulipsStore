from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tulips(models.Model):
    """Тюльпаны"""
    title = models.CharField("Название", max_length=200)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="tulips_image/")
    price = models.PositiveIntegerField("Цена", default=0)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tulip_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Тюльпан"
        verbose_name_plural = "Тюльпаны"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    tulip = models.ForeignKey(Tulips, on_delete=models.CASCADE, verbose_name="тюльпан")

    def __str__(self):
        return f"{self.star} - {self.tulip}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    tulip = models.ForeignKey(Tulips, verbose_name="тюльпан", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.tulip}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Zakaz(models.Model):
    mail = models.EmailField(blank=False)
    name = models.CharField("Ф.И.О.", max_length=300, blank=False)
    contacts = models.CharField("Телефон", max_length=20, blank=False)
    text = models.TextField(max_length=5000, blank=False)

    def __str__(self):
        return f"{self.name} - {self.contacts}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


