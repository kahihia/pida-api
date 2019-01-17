from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('products/',
         views.ProductList.as_view(),
         name='product-list'),
    path('products/<int:pk>/',
         views.ProductDetail.as_view(),
         name='category-detail'),
    path('companies/<int:pk>/',
         views.CompanyDetail.as_view(),
         name='company-detail'),
    path('categories/',
         views.CategoryList.as_view(),
         name='category-detail'),
    path('categories/<int:pk>/',
         views.CategoryDetail.as_view(),
         name='category-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)