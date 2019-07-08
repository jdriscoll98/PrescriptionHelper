from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from .forms import PrescriptionForm
from .models import Vitamin, Drug, Food
# -------------------------------------------------------------------------------
# Page Views
# -------------------------------------------------------------------------------


class HomePageView(TemplateView):
    template_name = 'website/homepage.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'form': PrescriptionForm,
            'list_of_drugs': Drug.objects.all()
        }
        return context

class ReturnSupplements(View):
    def post(self, *args, **kwargs):
        if self.request.is_ajax:
            data = {
                'success': False
            }
            try:
                drug = Drug.objects.filter(name=self.request.POST.get('name'))
                vitamin = Vitamin.objects.filter(drugs__in=drug).first()
                food = Food.objects.filter(drugs__in=drug).first()
            except Exception as e:
                print(e)
                messages.error(self.request, 'No drug found matching this name')
                return JsonResponse(data)
            data['success'] = True
            if vitamin:
                data['vitamin'] = vitamin.description
            if food:
                data['food'] = food.description
            return JsonResponse(data)
