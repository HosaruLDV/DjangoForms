from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render

from prod.forms import ProductForm, VersionForm
from prod.models import Product, Version
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse

# Create your views here.
class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('prod:product')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('prod:product')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('prod:product')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        FormSet = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()  # Student
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()  # Subject

        return super().form_valid(form)