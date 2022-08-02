
from django.urls import path, include

from .views import *

urlpatterns = [
    # allclient
    path('client', allclient, name="client"),
    #path('api/', include(router.urls)),
    path('', home, name="home"),
    path('<int:pk>/', ArticleDetail.as_view(), name="articles-detail"),
    path('article_form', ArticleCreateView.as_view(), name="articles-created"),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name="articles-updated"),
    path('<int:pk>/edit/staff/', ArticleStaffUpdateView.as_view(), name="articles-updated-staff"),
    # convention client
    path('clientconvention', listclientconvention, name="client-convention"),
    path('client-convention/<int:pk>/', DetailClientConvention.as_view(), name="client-convention-detail"),
    path('client-convention_form', ConventionEntrepriseClientCreateView.as_view(), name="client-convention-created"),
    # entreprise client
    path('entreprise', Entreprise_Client, name="entreprise"),
    path('entreprise/<int:pk>/', EntrepriseClientDetail.as_view(), name="entreprise-detail"),
    path('entreprise_form', EntrepriseClientCreateView.as_view(), name="entreprise-created"),
    # administration client
    path('adminstration', Administration_Client, name="administration"),
    path('adminstration/<int:pk>/', AdministrationClientDetail.as_view(), name="adminstration-detail"),
    path('adminstration_form', AdministrationClientCreateView.as_view(), name="adminstration-created"),
    # magazin
    path('shop', ShopList, name="Shop"),
    path('shop/<int:pk>/', ShopDetail.as_view(), name="shop-detail"),
    path('shop_form', ShopCreateView.as_view(), name="shop-created"),
    path('shop/<int:pk>/edit/', ShopUpdateView.as_view(), name="shop-update"),
    # category
    path('category', CategoryList, name="category"),
    path('category/<int:pk>/', CategoryDetail.as_view(), name="category-detail"),
    path('category_form', CategoryCreateView.as_view(), name="category-created"),
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name="category-updated"),
    
    #produit 
    path('product', ProductList, name="product"),
    path('product/<int:pk>/', ProductDetail.as_view(), name="product-detail"),
    path('product_form', ProductCreateView.as_view(), name="product-created"),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name="product-updated"),
    
    # clientparticluier
    path('clientparticluier', ClientParticulierList, name="clientparticluier"),
    path('clientparticluier/<int:pk>/', ClientParticulierDetail.as_view(), name="clientparticluier-detail"),
    path('clientparticluier_form', ClientParticulierCreateView.as_view(), name="clientparticluier-created"),
   
]
