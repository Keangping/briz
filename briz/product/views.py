from django.shortcuts import render, get_object_or_404
from .models import Dress, Seremoni, Skjorte, Sko, Smoking, Slips, Sloyfe, Mansjett, NewsImage, IndexContent, IndexProduct, Tip, Contact, Dressen_sitte, Dress_guide, Collection
from django.apps import apps

from itertools import chain	

def index(request):
	newsImage = NewsImage.objects.all()
	dresses = Dress.objects.all()[:5]
	seremonies = Seremoni.objects.all()[:5]
	smoking = Smoking.objects.all()[:5]
	indexProducts = list(chain(dresses, seremonies, smoking))
	indexContent = get_object_or_404(IndexContent, pk=1)
	return render(request, 'product/index.html', {'indexProducts':indexProducts, 'newsImage':newsImage, 'indexContent': indexContent})
	
def collection(request, product_type):
	# How do I retrieve a Django model class dynamically, use apps.get_model
	database_type = apps.get_model('product', product_type.title())
	gallery = database_type.objects.all()
	print gallery
	product = get_object_or_404(Collection, name=product_type)

	return render(request, 'product/collection.html', {'product':product, 'gallery':gallery, 'product_type':product_type})

def detail(request, product_type, product_id):
	# How do I retrieve a Django model class dynamically, use apps.get_model
	database_type = apps.get_model('product', product_type.title())
	product = get_object_or_404(database_type, pk=product_id)

	gallery = database_type.objects.all()

	pre_and_next = get_prev_and_next_items(product, gallery)
	pre = pre_and_next[0]
	next = pre_and_next[1]

	meta = product.description
	meta_des = product.product_type

	return render(request, 'product/detail.html', {'product':product, 'gallery':gallery, 'product_type':product_type, 'pre':pre, 'next':next, 'meta':meta, 'meta_des':meta_des})

def tips(request):
	tips = Tip.objects.all()
	return render(request, 'product/tips.html', {'tips':tips})

def dressen_sitte(request):
	tips = Dressen_sitte.objects.all()
	return render(request, 'product/dressen_sitte.html', {'tips':tips})

def dress_guide(request):
	tips = Dress_guide.objects.all()
	return render(request, 'product/dress_guide.html', {'tips':tips})

def contact(request):
	contact = Contact.objects.all().first()
	print contact
	return render(request, 'product/contact.html', {'contact':contact})

def get_prev_and_next_items(target, items):
    #To get previous and next objects from QuerySet
    found = False
    prev = None
    next = None
    for item in items:
        if found:
            next = item
            break
        if item.id == target.id:
            found = True
            continue
        prev = item
    return (prev, next)
