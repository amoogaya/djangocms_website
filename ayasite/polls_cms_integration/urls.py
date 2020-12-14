from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from .views import IndexView


app_name = 'polls'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

]

