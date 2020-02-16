from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import generic
from .models import TaxiOrder, Car
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import TaxiOrderForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import get_object_or_404
# Create your views here.


class OrdersView(LoginRequiredMixin, generic.ListView):
    model = TaxiOrder
    template_name = 'app/taxi/taxi_admin.html'
    context_object_name = 'orders'
    ordering = ['-pk']
    paginate_by = 3


class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaxiOrder
    template_name = 'app/taxi/order.html'


def order_form_creation(request):
    form = TaxiOrderForm()
    if request.method == 'POST':
        form = TaxiOrderForm(request.POST)
        if form.is_valid():
            if Car.objects.filter(active=True).exists():
                order_number = form.save()
                car = Car.objects.filter(active=True).first()
                car.active = False
                car.order = order_number
                car.save()
                messages.success(request, 'Ваше замовлення прийняте.')
                return render(request, 'app/taxi/success_order_info.html', {'order_number': order_number.pk,
                                                                            'car': car})
            else:
                messages.success(request, 'Нажаль, всі автомобілі зайняті.')
                return render(request, 'app/taxi/failed_order_info.html')
        else:
            form = TaxiOrderForm()

    context = {'form': form}
    return render(request, 'app/taxi/user_form_order.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('all_orders')
        else:
            messages.info(request, "Ім'я або пароль невірні")
            return render(request, 'app/taxi/login.html')

    return render(request, 'app/taxi/login.html')


def register_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'app/taxi/registration.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def change_taxi_state(request, brand='xxx'):
    # При добавленні кнопки в html
    # car1 = Car.objects.get(car_brand=brand)
    # car1.order = None
    # car1.active = True
    # return car1
    car = Car.objects.filter(active=False).first()
    car.order = None
    car.active = True
    car.save()
    return car
