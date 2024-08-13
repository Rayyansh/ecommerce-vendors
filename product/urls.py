from django.urls import path
from product.views import *

product = ProductViewSet.as_view({"get":"list","post":"create"})
slider = SliderViewSet.as_view({"get":"list","post":"create"})
main_category = MainCategoryViewSet.as_view({"get":"list","post":"create"})
category = CategoryViewSet.as_view({"get":"list","post":"create"})
brand = BrandViewSet.as_view({"get":"list","post":"create"})
product_review = ProductReviewViewSet.as_view({"get":"list","post":"create"})
wishlist = WishlistViewSet.as_view({"get":"list","post":"create"})

urlpatterns = [
    path('product/', product, name='product'),
    path('slider/', slider, name='slider'),
    path('main-category', main_category, name='main-category'),
    path('category', category, name='category'),
    path('brand', brand, name='brand'),
    path('product-review', product_review, name='product-review'),
    path('wishlist', wishlist, name='wishlist'),
]