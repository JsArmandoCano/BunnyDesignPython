from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib import messages
from .form import CommetsForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def Tarjetas(request, category=None):
    
    cat = None
    products = None
    
    if category != None:
        cat = get_object_or_404(CategoryTarjeta, category=category)
        products = ProductTarjeta.objects.filter(category=cat, is_available=True)
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()
        
    else:
        products = ProductTarjeta.objects.all().filter(is_available=True) 
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()
      
    categories = CategoryTarjeta.objects.all().filter(is_available=True) 
    
    # Formulario de Comenntarios
    form = CommetsForm()
    if request.method == 'POST':
        form = CommetsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message="Gracias por tu comentario!!!😍")
        return redirect('../')
            
    fav_commets = Comments.objects.all().filter(is_available=True).order_by('-created_date')[:3]
                
    return render(request, 'pages/tarjeta.html', {
        'categories': categories,
        'products': paged_products,
        'products_count': products_count,
        'cat': cat,
        'fav_commets': fav_commets,
        'form': form,
    })
    
    
def detail_tarjeta(request, category, slug):
    
    try: 
        single_product = ProductTarjeta.objects.get(category__category=category, slug=slug)
        
    except Exception as e:
        raise e
    
    product_gallery = ProductsGallery.objects.filter(product_id=single_product.id)
    
    return render(request, 'pages/detail.html', {
        'single_product': single_product,
        'product_gallery': product_gallery,
    })


# ---------------------------------------------------------
def Manualidad(request, category=None):
    
    cat = None
    products = None
    
    if category != None:
        cat = get_object_or_404(CategoryManualidades, category=category)
        products = ProductManualidades.objects.filter(category=cat, is_available=True)
        products_count = products.count()
        
    else:
        products = ProductManualidades.objects.all().filter(is_available=True) 
        products_count = products.count()
            
    categories = CategoryManualidades.objects.all().filter(is_available=True) 
    
    # Formulario de Comenntarios
    form = CommetsForm()
    if request.method == 'POST':
        form = CommetsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message="Gracias por tu comentario!!!😍")
        return redirect('../')

    fav_commets = Comments.objects.all().filter(is_available=True).order_by('-created_date')[:3]

    return render(request, 'pages/manualidad.html', {
        'categories': categories,
        'products': products,
        'products_count': products_count,
        'cat': cat,
        'fav_commets': fav_commets,
        'form': form,
    })
    
def detail_manu(request, category, slug):
    
    try: 
        single_product = ProductManualidades.objects.get(category__category=category, slug=slug)
        
    except Exception as e:
        raise e
    
    return render(request, 'pages/detail.html', {
        'single_product': single_product,
    })


# ---------------------------------------------------------
def DibyPins(request, category=None):
    
    cat = None
    products = None
    
    if category != None:
        cat = get_object_or_404(CategoryDibyPin, category=category)
        products = ProductDibyPin.objects.filter(category=cat, is_available=True)
        products_count = products.count()
        
    else:
        products = ProductDibyPin.objects.all().filter(is_available=True) 
        products_count = products.count()
        
    categories = CategoryDibyPin.objects.all().filter(is_available=True) 
    
    # Formulario de Comenntarios
    form = CommetsForm()
    if request.method == 'POST':
        form = CommetsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message="Gracias por tu comentario!!!😍")
        return redirect('../')

    fav_commets = Comments.objects.all().filter(is_available=True).order_by('-created_date')[:3]

    return render(request, 'pages/dibypin.html', {
        'categories': categories,
        'products': products,
        'products_count': products_count,
        'cat': cat,
        'fav_commets': fav_commets,
        'form': form,
    })
    
def detail_pin(request, category, slug):
    
    try: 
        single_product = ProductDibyPin.objects.get(category__category=category, slug=slug)
        
    except Exception as e:
        raise e
    
    return render(request, 'pages/detail.html', {
        'single_product': single_product,
    })


# ---------------------------------------------------------
def Telas(request, category=None):
    
    cat = None
    products = None
    
    if category != None:
        cat = get_object_or_404(CategoryTela, category=category)
        products = ProductTela.objects.filter(category=cat, is_available=True)
        products_count = products.count()
        
    else:
        products = ProductTela.objects.all().filter(is_available=True) 
        products_count = products.count()
    
    categories = CategoryTela.objects.all().filter(is_available=True) 
    
    # Formulario de Comenntarios
    form = CommetsForm()
    if request.method == 'POST':
        form = CommetsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message="Gracias por tu comentario!!!😍")
        return redirect('../')
    
    fav_commets = Comments.objects.all().filter(is_available=True).order_by('-created_date')[:3]

    return render(request, 'pages/tela.html', {
        'categories': categories,
        'products': products,
        'products_count': products_count,
        'cat': cat,
        'fav_commets': fav_commets,
        'form': form,
    }) 
    
def detail_tela(request, category, slug):
    
    try: 
        single_product = ProductTela.objects.get(category__category=category, slug=slug)
        
    except Exception as e:
        raise e
    
    return render(request, 'pages/detail.html', {
        'single_product': single_product,
    })
    

# Comentarios    
def all_commits(request):
    commits = Comments.objects.all().filter(is_available=True)
    
    return render(request, 'pages/all_commits.html', {
        'commits': commits,
    })