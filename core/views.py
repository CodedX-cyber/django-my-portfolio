from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_date(self, **kwargs):
        context = super().get_context_date(**kwargs) # first, call super get context data
        context['about'] = About.objects.first()
        context['services'] = Services.objects.all()
        context['works'] = RecentWorks.objects.all()
        return context
