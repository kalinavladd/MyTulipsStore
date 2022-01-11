from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.TulipsView.as_view()),
    path("all_tulips/", views.AllTulipsView.as_view(), name="all_tulips"),
    # path('filter/', views.FilterCategory.as_view(), name='filter'),
    path("add_zakaz/", views.ZakazReview.as_view(), name="add_zakaz"),
    path("<slug:slug>/", views.TulipsDetailView.as_view(), name="tulip_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),

]
