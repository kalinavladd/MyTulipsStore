from django import forms
from django.contrib import admin
# from django.contrib.gis import forms
from django.utils.safestring import mark_safe
from .models import Category, Tulips, RatingStar, Rating, Reviews, Zakaz
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)

class TulipsAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Tulips
        fields = '__all__'




# @admin.register(Category) альтернативный способ
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "id")
    list_display_links = ("name",)
    save_on_top = True
    save_as = True


class ReviewInLine(admin.StackedInline):
    """Класс, который позволяет при, открытие продукта видеть все
    прикрепленные к нему отзывы"""
    model = Reviews
    extra = 1
    """Указываем количество дополнительных полей (по умолчанию 4)
    TabularInline позволяет выстроить поля по горизонтали"""
    readonly_fields = ("name", "email")
    """Тоже делаем имя и имейл только для чтения"""


@admin.register(Tulips)
class TulipAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft", "get_image")
    list_filter = ("category", "price",)
    form = TulipsAdminForm
    # readonly_fields = ("get_image",)
    """Добавили фильтрацию по категории"""
    search_fields = ("title", "category__name")
    """Добавили поиск к нашим товарам(тюльпанам)
    # В категориях указываем что ищем по полю name через два __"""
    inlines = [ReviewInLine]
    """Указывая этот атрибут (М2М или FK) в списке передаем классы которые мы хотим к нам
    # прикрепить, (в данный момент для вывода отзывов вместе которые прикреплены к товару)"""
    save_on_top = True
    save_as = True
    actions = ["publish", "unpublish"]
    """Сохранить как новый объект"""
    list_editable = ("draft",)
    """Это позволит нам редактировать поле с галочкой (черновик) прям из списка товаров, через checkbox"""
    # fields = (("price", "category", "url"), )
    # """делаем в одну строку вывод, поля которые в кортеже не указаны не будут выведены"""
    fieldsets = (
        (None, {
            "fields": ("title", "description", "image")
        }),
        ("Опции", {
            "classes": ("collapse",),  # Эту группу мы делаем в свернутом виде
            "fields": (("price", "category", "url"),)
        }),
    )
    """Также можно использовать для размещения полей, а поместив кордеж, представим их в одну строку
    вместо None можем назвать категорию"""

    def get_image(self, image):
        return mark_safe(f'<img src={image.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"
    """Выводим изображение в админку, а метод потом передаем в list_display вместо поля image"""

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == '1':
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == '1':
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permission = ('change',)

    publish.short_description = "Снять с публикации"
    publish.allowed_permission = ('change',)

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "tulip", "id")
    readonly_fields = ("name", "email")
    """Указываем поля которые мы хотим скрыть от редактирования"""


@admin.register(Zakaz)
class ZakazAdmin(admin.ModelAdmin):
    list_display = ("name", "mail", "contacts", "text")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("tulip", "ip", "star")


admin.site.register(Category, CategoryAdmin)
# admin.site.register(Tulips) можно удалить, если зарегистрировали модель через декоратор
admin.site.register(RatingStar)
# admin.site.register(Rating)
# admin.site.register(Zakaz)
# admin.site.register(Reviews)


admin.site.site_title = "Django Tulips"
admin.site.site_header = "Django Tulips"
