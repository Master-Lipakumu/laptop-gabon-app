from django.shortcuts import render, redirect

# Create your views here.



from django.views.generic.detail import DetailView

from django.views.generic.list import ListView

# mes importations

from django.urls import reverse


from .models import (Shop, Category, Product, Articles, ConventionEntrepriseClient,
EntrepriseClient, AdministrationClient, DevisClient, ClientParticulier)


from django.contrib import messages

from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView, CreateView, DeleteView

from django.views.generic.edit import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

import random



###########################################################################################################

                     #   /***************UPDATE VIEW  ******************/

##########################################################################################################

class ShopUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Shop
    fields = ['shop_image','name','description','responsable_name','active','email','phone_number','localisation']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class CategoryUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Category
    fields = ['name','description','active','shop']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False




class ProductUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Product
    fields = ['name','description','active','category']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Articles
    fields = ['model','name','description','article_image','active','price','stock','article_id','product']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class ArticleStaffUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Articles
    fields = ['facture','devisClientType','bonlivraison','quantite_client']

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False









###########################################################################################################

                     #   /***************FIN DES CREATIONS  ******************/

##########################################################################################################






###########################################################################################################

                     #   /***************CREATION  ******************/

##########################################################################################################

class ArticleCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Articles
    fields = ['model','name','description','article_image','active','price','stock','article_id','product']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def choices():
        list1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,25,29,30,31,32,33,34,
        35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,56,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,
        73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,88,90,91,92,93,94,95,96,97,98,99,100]
        r1 = random.randint(0, 14)
        return {'r1':r1}




class ShopCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Shop
    fields = ['shop_image','name','description','responsable_name','active','email','phone_number','localisation']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False




class CategoryCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Category
    fields = ['name','description','active','shop']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False





class ProductCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Product
    fields = ['name','description','active','category']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False





class ClientParticulierCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = ClientParticulier
    fields = ['client_Name','address','client_Number_id','postal_Code','phone_number','email_Address',
    'facture','devisClient_particulier','bonlivraison_client_particulier']

    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False




class AdministrationClientCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = AdministrationClient
    fields = ['nation_choices','client_Name','address','postal_Code','phone_number','email_Address',
    'facture','partenary_code','taxe_TPS','taxe_CSS','remise','livraison','modalite_paiement','devisadministrationClient',
    'bonlivraison_administration']

    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False






class ConventionEntrepriseClientCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = ConventionEntrepriseClient
    fields = ['nation_choices','client_Name','address','postal_Code','phone_number','email_Address',
    'facture','partenary_code','taxe_TPS','taxe_CSS','remise','livraison','modalite_paiement','devisconventionentrepriseClient',
    'bonlivraison_convention_entreprise']

    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False






class EntrepriseClientCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = EntrepriseClient
    fields = ['nation_choices','client_Name','address','postal_Code','phone_number','email_Address',
    'facture','partenary_code','taxe_TPS','taxe_CSS','remise','livraison','modalite_paiement','devisentrepriseClient',
    'bonlivraison_entreprise']

    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False




###########################################################################################################

                     #   /***************FIN DES CREATIONS  ******************/

##########################################################################################################

def allclient(request):

    return render(request,'alldetail/allclient.html')



###########################################################################################################

                     #   /***************PRODUCT ******************/

##########################################################################################################


def ProductList(request):

    products = Product.objects.all().order_by('-date_created')

    products = list(products)

    total_number = Product.objects.all().count

    context = {"products": products, "total_number":total_number}

    return render(request, "alldetail/products_list.html", context)

class ProductDetail(DetailView):

    templates_name = "alldetail/product_detail.html"

    model = Product

###########################################################################################################

                     #   /***************Category ******************/

##########################################################################################################


def CategoryList(request):

    categorys = Category.objects.all().order_by('-date_created')

    categorys = list(categorys)

    total_number = Category.objects.all().count()

    context = {"categorys": categorys}

    return render(request, "alldetail/categorys_list.html", context)

class CategoryDetail(DetailView):

    templates_name = "alldetail/category_detail.html"

    model = Category

###########################################################################################################

                     #   /***************SHOP ******************/

##########################################################################################################


def ShopList(request):

    shops = Shop.objects.all().order_by('-date_created')

    shops = list(shops)

    total_number = Shop.objects.all().count()

    context = {"shops": shops,"total_number":total_number}

    return render(request, "alldetail/shops_list.html", context)

class ShopDetail(DetailView):

    templates_name = "alldetail/shop_detail.html"

    model = Shop

###########################################################################################################

                     #   /***************ENTREPRISE CONVENTION CLIENT ******************/

##########################################################################################################


def listclientconvention(request):

    conventionclient = ConventionEntrepriseClient.objects.all()

    conventionclient = list(conventionclient)

    total_number = ConventionEntrepriseClient.objects.all().count()

    context = {"conventionclient": conventionclient, "total_number":total_number}

    return render(request, "alldetail/convention_client_list.html", context)

class DetailClientConvention(DetailView):

    templates_name = "alldetail/convention_client_detail.html"

    model = ConventionEntrepriseClient





###########################################################################################################

                      #  /***************ARTICLE  ******************/
##########################################################################################################


def home(request):

    articles = Articles.objects.all().order_by('-date_created')

    articles = list(articles)

    total_number = Articles.objects.all().count()

    context = {"articles": articles, "total_number":total_number}

    return render(request, "alldetail/index.html", context)

class ArticleDetail(DetailView):

    templates_name = "alldetail/articles_detail.html"

    model = Articles





###########################################################################################################

                      #  /***************Entreprise client ******************/
##########################################################################################################


def Entreprise_Client(request):

    entreprise_clients = EntrepriseClient.objects.all()

    entreprise_clients= list(entreprise_clients)

    total_number = EntrepriseClient.objects.all().count()

    context = {"entreprise_clients": entreprise_clients, "total_number":total_number}

    return render(request, "alldetail/entreprise_client_list.html", context)

class EntrepriseClientDetail(DetailView):

    templates_name = "alldetail/entrepriseclient_detail.html"

    model = EntrepriseClient




###########################################################################################################

                      #  /***************administraction client ******************/
##########################################################################################################


def Administration_Client(request):

    administrationClient = AdministrationClient.objects.all()

    administrationClient = list(administrationClient)

    total_number = AdministrationClient.objects.all().count()

    context = {"administrationClient": administrationClient, "total_number":total_number}

    return render(request, "alldetail/administration_client_list.html", context)

class AdministrationClientDetail(DetailView):

    templates_name = "alldetail/administractionclient_detail.html"

    model = AdministrationClient



###########################################################################################################

                     #   /***************ClientParticulier ******************/

##########################################################################################################


def ClientParticulierList(request):

    clientsparticulier = ClientParticulier.objects.all()

    clientsparticulier= list(clientsparticulier)

    clientsparticulier_total_number = ClientParticulier.objects.all().count()

    context = {"clientsparticulier": clientsparticulier,
    "clientsparticulier_total_number":clientsparticulier_total_number}

    return render(request, "alldetail/clientsparticulier_list.html", context)

class ClientParticulierDetail(DetailView):

    templates_name = "alldetail/clientparticulier_detail.html"

    model = ClientParticulier