from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView


class IndexView(ListView):
    template = 'polls_cms_integration/index.html'
