from django.shortcuts import render
from .forms import OrderForm
from django.views import View

from .models import Order


# Create your views here.

class Home(View):
    def get(self, request):
        form = OrderForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        print(request.POST)
        form = OrderForm(request.POST)

        if form.is_valid():
            print("Form is valid")
            order = Order(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                interests=form.cleaned_data['interests'],
                message=form.cleaned_data['message']
            )
            order.save()
            print(form.cleaned_data)  # فقط برای تست
        else:
            # چاپ ارورهای فرم
            print("Form is invalid")
            print(form.errors)  # چاپ ارورهای فرم

        return render(request, 'index.html', {'form': form})
