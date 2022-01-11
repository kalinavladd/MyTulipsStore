from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View, TemplateView
from .models import Tulips, Category
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import ReviewForm, ZakazForm, RatingForm


class GategoriesList:
    def get_categor(self):
        return Category.objects.all()

    def get_tulip(self):
        return Tulips.objects.filter(draft=False)


# class FilterCategory(GategoriesList, ListView):
#     """Фильтр тюльпанов"""
#     def get_queryset(self):
#         queryset = Tulips.objects.filter(category__in=self.request.GET.getlist("category"))
#         return queryset

    # Тут мы фильтруем и если категори которая приходит с фронта находится, мы достаем все значение тбльпана по тайтлу


class TulipsView(GategoriesList, ListView):
    """Список тюльпанов"""
    model = Tulips
    # queryset = Tulips.objects.all()
    queryset = Tulips.objects.filter(draft=False)  # Фильтруем и не выводим поле с черновиками
    template_name = "tulips/index.html"
    # paginate_by = 6


class AllTulipsView(GategoriesList, ListView):
    """Все позиции цветов"""
    model = Tulips
    queryset = Tulips.objects.filter(draft=False)
    template_name = "tulips/all_tulips.html"
    context_object_name = 'all_tulips'
    paginate_by = 6


class TulipsDetailView(DetailView):
    """Полное описание цветка"""
    model = Tulips
    slug_field = "url"
    template_name = "tulips/tulips.html"
    context_object_name = "tulip"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        return context


# class AddReview(View):
#     """Отзывы"""
#     def post(self, requests, pk):
#         form = ReviewForm(requests.POST)
#         if form.is_valid():
#             form = form.save(commit=False)  # говорим что мы хотим приостановить сохранение нашей
#             # формы, чтоб внести в неё некие изменения
#             form.tulip_id = pk  # в поле tulips мы должны указать объект к которому хотим привязаться
#             # но так как у нас есть только id (pk) нашего тюльпана, напрямую в это поле мы не можем передать данное
#             # число, мы должны сюда передавать обьект нашего цветка но можем через _id указать наше значение
#             form.save() # теперь данные с формы будут записаны в базу (tulips_id мы взяли из нащей базы tulips_reviews)
#         return redirect("/")


class AddReview(View):
    """Отзывы второй вариант"""
    def post(self, requests, pk):
        form = ReviewForm(requests.POST)
        tulip = Tulips.objects.get(id=pk)  # делая запрос в БД и найди наш фильм по id мы получаем
        # наш объект тюльпана
        if form.is_valid():
            form = form.save(commit=False)  # говорим что мы хотим приостановить сохранение нашей
            # формы, чтоб внести в неё некие изменения
            form.tulip = tulip  # тут мы присваиваем наш объект
            if requests.POST.get("parent", None):
                form.parent_id = int(requests.POST.get("parent"))
                """parent это имя нашего поля в верстке, если оно будет мы выполним код, если None то ничего не произойдет
                далее parent_id (id потому что мы будем добавлять число а не объект), мы достаем значение нашего ключа parent
                но так как оно строковое мы оборачиваем его в инт"""
            form.save()
        return redirect(tulip.get_absolute_url())


class ZakazReview(View):
    def post(self, request):
        if request.method == "POST":
            form = ZakazForm(request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect("/")
        # else:
        #     form = ZakazForm()
        # return render(request, "include/footer.html", {"form": form})

# class TulipsView(View):
#     """Список тюльпанов"""
#     def get(self, requests):
#         tulips = Tulips.objects.all()
#         return render(requests, "tulips/index.html", {"tulips_list": tulips})
#
#
#
# class TulipsDetailView(View):
#     """Полное описание цветка"""
#     def get(self, requests, slug):
#         tulip = Tulips.objects.get(url=slug)
#         return render(requests, "tulips/tulips.html", {"tulip": tulip})
