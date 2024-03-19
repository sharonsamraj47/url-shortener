
from django.urls import include, path

from .views import wildcard_redirect

urlpatterns = [
    path(r"^(?P<path>.*)", wildcard_redirect),

]