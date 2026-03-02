from django.shortcuts import render,redirect
from core.decorators import seller_required
from django.contrib.auth.decorators import login_required
from .models import SellerProfile,Product,SubCategory,Attribute,VariantAttributeBridge,ProductVariant,Category

@login_required
@seller_required
def seller_profile_view(request):
    profile, _ = SellerProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":

        profile.store_name = request.POST.get("store_name")
        profile.store_slug = request.POST.get("store_slug")
        profile.gst_number = request.POST.get("gst_number")
        profile.pan_number = request.POST.get("pan_number")
        profile.bank_account_number = request.POST.get("bank_account_number")
        profile.ifsc_code = request.POST.get("ifsc_code")
        profile.business_address = request.POST.get("business_address")

        
        if request.FILES.get("store_image"):
            profile.store_image = request.FILES.get("store_image")

        profile.save()
        return redirect('dashboard')

    return render(request, "seller_templates/sellerprofilepage.html", {"profile": profile})

@login_required
def dashboard_view(request):
    seller = request.user.seller_profile
    products = Product.objects.filter(seller=seller).order_by('-id')  
    return render(request, "seller_templates/sellerdashboard.html", {"products": products})

def seller_bridge(request):
    user=request.user
    if user.is_authenticated:
        if SellerProfile.objects.filter(user=request.user).exists():
            return redirect("dashboard")

        if request.method == "POST": 
            store_name = request.POST.get("store_name")
            gst_number = request.POST.get("gst_number")
            pan_number = request.POST.get("pan_number")
            bank_account_number = request.POST.get("bank_account_number")
            ifsc_code = request.POST.get("ifsc_code")
            business_address = request.POST.get("business_address")
            store_image = request.FILES.get("store_image")
    return render(request, "seller_templates/seller_bridge.html")


@login_required
def add_product(request):
    seller = request.user.seller_profile
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    attributes = Attribute.objects.prefetch_related("options").all()

    if request.method == "POST":
        
        product = Product.objects.create(
            seller=seller,
            subcategory_id=request.POST.get("subcategory"),
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            brand=request.POST.get("brand"),
            model_number=request.POST.get("model_number")
        )

        
        variant = ProductVariant.objects.create(
            product=product,
            mrp=request.POST.get("mrp") or 0,
            selling_price=request.POST.get("selling_price") or 0,
            cost_price=request.POST.get("cost_price") or 0,
            stock_quantity=request.POST.get("stock_quantity") or 0,
            weight=request.POST.get("weight") or 0,
            length=request.POST.get("length") or 0,
            width=request.POST.get("width") or 0,
            height=request.POST.get("height") or 0,
            tax_percentage=request.POST.get("tax_percentage") or 0
        )

        
        for attribute in attributes:
            option_id = request.POST.get(f"attribute_{attribute.id}")
            if option_id:
                VariantAttributeBridge.objects.create(
                    variant=variant,
                    option_id=option_id
                )
        return redirect("dashboard")  

    
    context = {"categories": categories,"subcategories": subcategories, "attributes": attributes }
    return render(request, "seller_templates/productapppage.html", context)
