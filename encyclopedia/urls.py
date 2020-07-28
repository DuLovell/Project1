from django.urls import path

from . import views

app_name="encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    # wiki/search/ path
    # wiki/create/ path
    path("<str:entry>", views.entry , name="entry"),
]
