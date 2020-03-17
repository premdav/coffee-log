from django.shortcuts import render, redirect
from .models import Coffee
from .forms import CreateCoffee
from django.http import HttpResponse, JsonResponse
from django.core import serializers

def index(request):
  coffee_collection = Coffee.objects.all()
  print(coffee_collection)
  return render(request, 'coffee/collection.html', { 'all_coffee': coffee_collection })

def add_coffee(request):
  new_coffee = CreateCoffee()
  if request.method == 'POST':
    new_coffee = CreateCoffee(request.POST, request.FILES)
    if new_coffee.is_valid():
      new_coffee.save()
      return redirect('index')
    else:
      return HttpResponse('''The form was filled out incorrectly, please <a href={{url: "index"}}>reload</a>''')
  else:
    return render(request, 'coffee/coffee_form.html', {'c_form': new_coffee})

def update_coffee(request, coffee_id):
  c_id = int(coffee_id)
  try:
    selected_coffee = Coffee.objects.get(id = c_id)
  except Coffee.DoesNotExist:
    return redirect('index')
  coffee_form = CreateCoffee(request.POST or None, instance = selected_coffee)
  if coffee_form.is_valid():
    coffee_form.save()
    return redirect('index')
  return render(request, 'coffee/coffee_form.html', {'c_form': coffee_form})

def delete_coffee(request, coffee_id):
  if request.method == 'DELETE':
    print(request)
    c_id = int(coffee_id)
    try:
      selected_coffee = Coffee.objects.get(id = c_id)
    except Coffee.DoesNotExist:
      return redirect('index')
    selected_coffee.delete()
    return redirect('index')
  return redirect('index')
