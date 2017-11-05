from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def restaurant_list(request):
	object_list = Restaurant.objects.all()

	paginator = Paginator(object_list, 5)
	page = request.GET.get('page')
	try:
		objects = paginator.page(page)
	except PageNotAnInteger:
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)

	context = {
		"objects":objects,
	}
	return render(request, 'restaurant_list.html', context)

def restaurant_detail(request, restaurant_id):
    instance = Restaurant.objects.get(id=restaurant_id)
    context = {
    "restaurant": instance
    }
    return render(request, 'restaurant_detail.html', context)

def restaurant_create(request):
    form = RestaurantForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("restaurant_list")
    context = {
    "form": form,
    }
    return render(request, 'restaurant_create.html', context)

def restaurant_update(request, restaurant_id):
    instance = Restaurant.objects.get(id=restaurant_id)
    form = RestaurantForm(request.POST or None, request.FILES or None, instance = instance)
    if form.is_valid():
        form.save()
        return redirect("restaurant_detail", restaurant_id=instance.id)
    context = {
    "form":form,
    "instance": instance,
    }
    return render(request, 'restaurant_update.html', context)

def restaurant_delete(request, restaurant_id):
    instance = Restaurant.objects.get(id=restaurant_id)
    instance.delete()
    return redirect("restaurant_list")
