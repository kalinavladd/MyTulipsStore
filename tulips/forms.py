from django import forms
from .models import Reviews, Zakaz, Rating, RatingStar



class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:  # указываем от какой модели нам нужно строить форму
        model = Reviews
        # указываем поля из модели которые мы хотим видеть в нашей форме
        fields = ("name", "email", "text")


class ZakazForm(forms.ModelForm):
    class Meta:
        model = Zakaz
        fields = ("mail", "name", "contacts", "text")


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)