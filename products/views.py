from django.shortcuts import render, redirect
from .models import Product, MainCategory, Category, SubCategory, Brand, ProductSize, Color, ProductGallery
from django.contrib import messages

from main.decorators import allowed_group

# Create your views here.

@allowed_group('Seller')
def adding_product(request):

    try:
        if request.method == 'POST':
            main_category = MainCategory.objects.get(value=request.POST.get('main_category_id'))
            category = Category.objects.get(value=request.POST.get('category_id'))
            sub_category = SubCategory.objects.get(value=request.POST.get('subcategory_id'))
            brand_name = Brand.objects.get(value=request.POST.get('brand_id'))
            product_name = request.POST.get('product_name')
            model_number = request.POST.get('model_no')
            short_desc = request.POST.get('short_desc')
            long_desc = request.POST.get('long_desc')
            specification = request.POST.get('specification')
            min_order_quantity = request.POST.get('min_order')
            quantity_unit = request.POST.get('quantity_unit')
            product_size = []
            for i in request.POST.getlist('sizeof[]'):
                product_size.append(ProductSize.objects.get(value=i).size)
            product_size = ", ".join(product_size)
            product_price = ", ".join(request.POST.getlist('prod_price[]'))
            min_quantity = ", ".join(request.POST.getlist('prod_qty[]'))
            max_quantity = ", ".join(request.POST.getlist('price_qty_max[]'))
            stock = True
            if request.POST.get('stock') == 'Out of Stock':
                stock = False

            product_pic = request.FILES['image']

            user = request.user

            # print(main_category)
            # print(category)
            # print(sub_category)
            # print(brand_name)
            # print(product_name)
            # print(model_number)
            # print(short_desc)
            # print(long_desc)
            # print(specification)
            # print(min_order_quantity)
            # print(quantity_unit)
            # print(product_size)
            # print(product_price)
            # print(min_quantity)
            # print(max_quantity)
            # print(stock)
            # print(user)

            product = Product.objects.create(
                main_category=main_category,
                category=category,
                sub_category=sub_category,
                brand_name=brand_name,
                product_name=product_name,
                model_number=model_number,
                short_description=short_desc,
                long_description=long_desc,
                specification=specification,
                min_order_quantity=min_order_quantity,
                quantity_unit=quantity_unit,
                product_size=product_size,
                price=product_price,
                min_quantity=min_quantity,
                max_quantity=max_quantity,
                in_stock=stock,
                product_pic=product_pic,
                supplier=user
            )

            colors = request.POST.getlist('colorof[]')

            for i in range(1, 100):
                try:
                    photo = request.FILES[f'photo_gallery_{i}']
                    ProductGallery.objects.create(image=photo, product=product, color=Color.objects.get(value=colors[i-1]))

                except:
                    break

            context = {'msg': short_desc}
            messages.success(request, 'Product added successfully')
            return redirect('product-listing')

    except:
        messages.error(request, 'Could not add product. Please try again.')

    return redirect('product-listing')

@allowed_group('Seller')
def status_change(request, id):

    product = Product.objects.get(id=id)
    status = product.status
    if status:
        product.status = False
    else:
        product.status = True

    product.save()
    return redirect('product-listing')


@allowed_group('Seller')
def delete_product(request, id):
    
    Product.objects.get(id=id).delete()
    messages.success(request, 'Product deleted.')
    return redirect('product-listing')

@allowed_group('Seller')
def update_product(request, id):

    try:
        if request.method == "POST":
            main_category = MainCategory.objects.get(value=request.POST.get('main_category_id'))
            category = Category.objects.get(value=request.POST.get('category_id'))
            sub_category = SubCategory.objects.get(value=request.POST.get('subcategory_id'))
            brand_name = Brand.objects.get(value=request.POST.get('brand_id'))
            product_name = request.POST.get('product_name')
            model_number = request.POST.get('model_no')
            short_desc = request.POST.get('short_desc')
            long_desc = request.POST.get('long_desc')
            specification = request.POST.get('specification')
            min_order_quantity = request.POST.get('min_order')
            quantity_unit = request.POST.get('quantity_unit')
            product_size = []
            for i in request.POST.getlist('sizeof[]'):
                product_size.append(ProductSize.objects.get(value=i).size)
            product_size = ", ".join(product_size)
            product_price = ", ".join(request.POST.getlist('prod_price[]'))
            min_quantity = ", ".join(request.POST.getlist('prod_qty[]'))
            max_quantity = ", ".join(request.POST.getlist('price_qty_max[]'))
            stock = True

            if request.POST.get('stock') == 'Out of Stock':
                stock = False

            product = Product.objects.get(id=id)
            product.main_category=main_category
            product.category=category
            product.sub_category=sub_category
            product.brand_name=brand_name
            product.product_name=product_name
            product.model_number=model_number
            product.short_description=short_desc
            product.long_description=long_desc
            product.specification=specification
            product.min_order_quantity=min_order_quantity
            product.quantity_unit=quantity_unit
            product.product_size=product_size
            product.price=product_price
            product.min_quantity=min_quantity
            product.max_quantity=max_quantity
            product.in_stock=stock

            try:
                product_pic = request.FILES['image']
                product.product_pic = product_pic
            except:
                pass

            colors = request.POST.getlist('colorof[]')

            for i in range(1, 100):
                try:
                    photo = request.FILES[f'photo_gallery_{i}']
                    if Color.objects.filter(value=colors[i-1]).exists():
                        ProductGallery.objects.create(image=photo, product=product, color=Color.objects.get(value=colors[i-1]))
                    
                    else:
                        ProductGallery.objects.create(image=photo, product=product)

                except:
                    break

            product.save()
            messages.success(request, 'Product updated successfully.')

            return redirect('product-listing')

    except:
        messages.warning(request, 'Could not update product, please try again.')
        return redirect('product-listing')
    
    product = Product.objects.get(id=id)
    sizes = list(product.product_size.split(', '))
    values = []
    for size in sizes:
        try:
            values.append(ProductSize.objects.get(size=size).value)
        except:
            pass

    values = ", ".join(values)

    photos = ProductGallery.objects.filter(product=product)

    context = {'product': product, 'values':values, 'photos': photos}

    return render(request, 'main/edit-product.html', context)

@allowed_group('Seller')
def delete_photo_gallery(request, id):
    
    ProductGallery.objects.get(id=id).delete()
    messages.success(request, 'Photo deleted.')
    return redirect('product-listing')

    
def crunch(name):
    name = name.replace(' ', '')
    name = name.replace(',', '')
    name = name.replace('&', '')
    name = name.replace('-', '')
    name = name.replace('.', '')
    name = name.replace("'", '')
    name = name.replace('/', '')
    name = name.lower()

    return name

def product_details(request, category, product_name):

    product = Product.objects.get(product_name=product_name)
    product_pics = ProductGallery.objects.filter(product=product)

    colors = []
    l = len(product_pics)
    for i in range(l):
        try:
            if product_pics[i].color.name not in colors:
                colors.append(product_pics[i].color.name)
        except:
            pass

    colors = [i.title() for i in colors]

    related_products = Product.objects.filter(category= Category.objects.get(name= category)).exclude(product_name=product_name)

    context = {'product': product, 'product_pics': product_pics, 'colors': colors, 'related_products': related_products}
    return render(request, 'main/product.html', context)


# def category_products(request, category):

#     print(category)
#     return render(request, 'main/products-by-category.html')