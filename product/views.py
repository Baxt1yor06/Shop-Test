from django.shortcuts import render

from .models import *
from product.forms import ContactForm
from django.views.generic import View
from django.http import HttpResponseRedirect

def index(request):
    products = Product.objects.all() 
    context = {
        'products': products
    }
    return render(request,'index.html', context=context)

def detail(request, id):
    details = Product.objects.get(id=id)
    related_products = Product.objects.filter(category=details.category).exclude(id=details.id)
    context = {
    'details': details,
    'related_products': related_products
    }
    return render(request,'detail.html', context=context)


# def about(request):
#     print(request.method)
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             if form.cleaned_data['number'] != "+998333265152":
#                 Contact.objects.create(
#                     name = form.cleaned_data['name'],
#                     email = form.cleaned_data['email'],
#                     number = form.cleaned_data['number'],
#                     gender = form.cleaned_data['gender'],
#                     message = form.cleaned_data['message']                    
#                 )
#                 print("Success")
#             else:
#                 print('Block')
#         else:
#             print('Error')
#     context = {
#         'form': form
#     }
#     return render(request,'about.html' , context=context)
        
    
class ContactView(View):
    form_class = ContactForm
    initial = {"key" : "value"}
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    
    def post(self, request, *args, **kwargs):
        form  = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("")
        
        
        return render(request, self.template_name, {'form': form})
        


