from django.db import models

# Create your models here.

class Contact(models.Model):
    """Подписка по емейл"""
    name = models.CharField(max_length=250)
    text = models.TextField()
    contact = models.CharField("Телефон", max_length=20, blank=False)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email