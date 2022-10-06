from dataclasses import fields
from re import template
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Keycaps, Reviews
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.

#! ---------------------- Home/About ROUTES ----------------------

class Home(TemplateView):
    template_name='home.html'


class About(TemplateView):
    template_name='about.html'


# ! ---------------------- PRODUCTS ROUTES ----------------------
class Products(TemplateView):
    template_name='products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")

        if name != None:
            context["keycaps"] = Keycaps.objects.filter(name__icontains = name)
            context["stuff_at_top"] = f'Seatching through Keycaps list for {name}'
            print('this hits',context)
        else:
            context["keycaps"] = Keycaps.objects.all()
            context["stuff_at_top"] = "Keycap Selection"
            print('this hits',context)
        return context

class ProductDetail(DetailView):
    model = Keycaps
    template_name = "products_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Reviews.objects.filter()
        return context

class ProductsCreate(CreateView):
    model = Keycaps
    fields = ['name', 'img', 'info', 'available_keycap']
    template_name = 'products_create.html'
    success_url = "/products/"

class ProductsDelete(DeleteView):
    model = Keycaps
    template_name = "products_delete.html"
    success_url = '/products/'

class ProductsUpdate(UpdateView):
    model = Keycaps
    fields = ['name', 'img', 'info', 'available_keycap',]
    template_name= 'products_update.html'
    success_url= "/products/"

    def get_success_url(self):
        return reverse('products_detail', kwargs={'pk': self.object.pk})

#! ---------------------- REVIEWS ROUTES ----------------------
class ReviewsDetail(DetailView):
    model = Reviews
    template_name= 'reviews_detail.html'

class ReviewCreate(View):
    def post(self, request, pk):
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        keycap = Keycaps.objects.get(pk=pk)
        Reviews.objects.create(rating=rating, comment=comment, keycap=keycap)
        return redirect('products_detail', pk=pk)

# class ReviewsCreate(CreateView):
#     model = Reviews
#     fields = ['rating', 'comment']
#     template_name = 'reviews_create.html'
#     success_url = "/products/<int:pk>"
#     # * Do I need more things here?

# class ReviewsDelete(DeleteView):
#     model = Reviews
#     template_name = "reviews_delete.html"
#     success_url = "/products/<int:pk>"

# class ReviewsUpdate(UpdateView):
#     model = Reviews
#     fields = ['name', 'img', 'info', 'available_keycap',]
#     template_name= 'reviews_update.html'
#     success_url= "/products/<int:pk>"

    # def get_success_url(self):
    #     return reverse('reviews_detail', kwargs={'pk': self.object.pk})