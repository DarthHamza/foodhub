from django.shortcuts import render
from .models import Restaurant

def restaurant_list(request):
	object_list = Restaurant.objects.all()
	context = {
		"objects":object_list,
	}
	return render(request, 'restaurant_list.html', context)

def restaurant_detail(request, restaurant_id):
    instance = Restaurant.objects.get(id=restaurant_id)
    context = {
    "restaurant": instance
    }
    return render(request, 'restaurant_detail.html', context)