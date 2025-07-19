from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def product_list(request, cat_slug=None):
    cat = None
    products = Product.objects.filter(available=True)
    cats = Category.objects.all()
    
    if cat_slug:
        cat = get_object_or_404(Category, slug=cat_slug)
        products = products.filter(category = cat)
        
    return render(request, "products/product/list.html", {
        'products': products,
        'category': cat,
        'categories': cats,
    })
    
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    
    return render(request, "products/product/detail.html", {
        'product': product,
    })