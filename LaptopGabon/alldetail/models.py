from django.db import models, transaction

# Create your models here.

from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField

import barcode

from barcode.writer import ImageWriter

from io import BytesIO

from django.core.files import File

from docuclient.models import Facture, BonLivraison, DevisClient, Ravite

from django.urls import reverse


# Create your models here.

User = get_user_model()



""" 

########################################################################################################


              #  /***************** BOUTIQUE DATA BASE ********************/
########################################################################################################



"""

class Shop(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)

    date_updated = models.DateTimeField(auto_now=True)

    shop_image = models.ImageField(upload_to='shopimages/')

    name = models.CharField(max_length=255)

    responsable_name = models.CharField(max_length=255)

    email = models.EmailField(max_length = 254)

    phone_number = PhoneNumberField()

    description = models.TextField(blank=True)

    localisation = models.CharField(max_length = 255)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    active = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("shop-detail", kwargs = {"pk":self.pk})

    def __str__(self):

        return self.name

    @transaction.atomic
    def disable(self):

        if self.active is False:

            return

        self.active = False

        self.save()

        self.categorys.update(active=False)


""" 

########################################################################################################


             #   /***************** CATEGORY DATA BASE ********************/
########################################################################################################



"""




class Category(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)

    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    active = models.BooleanField(default=False)

    shop = models.ForeignKey('alldetail.Shop', on_delete=models.CASCADE, related_name='categorys')

    def get_absolute_url(self):
        return reverse("category-detail", kwargs = {"pk":self.pk})

    def __str__(self):

        return self.name

    @transaction.atomic
    def disable(self):

        if self.active is False:

            return
        self.active = False

        self.save()

        self.products.update(active=False)




""" 

########################################################################################################


             #  /***************** PRODUCT DATA BASE ********************/
########################################################################################################



"""




class Product(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)

    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    active = models.BooleanField(default=False)

    category = models.ForeignKey('alldetail.Category', on_delete=models.CASCADE, related_name='products')

    def get_absolute_url(self):
        return reverse("product-detail", kwargs = {"pk":self.pk})

    def __str__(self):

        return self.name

    @transaction.atomic
    def disable(self):

        if self.active is False:

            return

        self.active = False

        self.save()

        self.articles.update(active=False)




""" 

########################################################################################################


             #   /***************** CLIENT Particulier data BASE ********************/
########################################################################################################



"""

class ClientParticulier(models.Model):

    #Basic Fields.
    client_Name = models.CharField(null=True, blank=True, max_length=200)

    client_Number_id = models.CharField(null=True, blank=True, max_length=200)

    address = models.CharField(null=True, blank=True, max_length=255)

    postal_Code = models.CharField(null=True, blank=True, max_length=10)

    phone_number = PhoneNumberField()

    email_Address = models.EmailField(null=True, blank=True, max_length=200)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    facture = models.ForeignKey('docuclient.Facture', on_delete=models.CASCADE, null = True, blank = True, related_name='facture_client_particulier')

    devisClient_particulier = models.ForeignKey(DevisClient, on_delete = models.SET_NULL, null = True, blank = True, related_name = "devisClient_particulier")

    bonlivraison_client_particulier = models.ForeignKey(BonLivraison, on_delete = models.SET_NULL, null = True, blank = True, related_name = "bonlivraison_client_particulier")

    date_created = models.DateTimeField(auto_now_add = True)

    last_updated = models.DateTimeField(auto_now = True)

    def get_absolute_url(self):
        return reverse("clientparticulier-detail", kwargs = {"pk":self.pk})

    def __str__(self):
        return f'document type {self.client_Name}, client type{self.phone_number}'





""" 

########################################################################################################


             #   /***************** CLIENT administration DATA BASE ********************/
########################################################################################################



"""

class AdministrationClient(models.Model):

    NATION = [
        ('National', 'National'),
        ('International', 'International'),
    ]

    nation_choices = models.CharField(choices=NATION, blank=True, null=True, max_length=100)

    client_Name = models.CharField(null=True, blank=True, max_length=200)

    address = models.CharField(null=True, blank=True, max_length=255)

    postal_Code = models.CharField(null=True, blank=True, max_length=10)

    phone_number = PhoneNumberField()

    email_Address = models.EmailField(null=True, blank=True, max_length=200)

    partenary_code = models.CharField(max_length = 200, blank = True, null=True)

    taxe_TPS = models.FloatField(null=True, blank=True)

    taxe_CSS = models.FloatField(null=True, blank=True)

    remise = models.FloatField(null=True, blank=True)

    livraison = models.CharField(null=True, blank=True, max_length=200)

    modalite_paiement = models.FloatField(blank=True, null=True)

    devisadministrationClient = models.ForeignKey(DevisClient, on_delete = models.SET_NULL, null = True, blank = True, related_name = "devisadministrationClient")

    bonlivraison_administration = models.ForeignKey(BonLivraison, on_delete = models.SET_NULL, null = True, blank = True, related_name = "bonlivraison_administration")

    facture = models.ForeignKey('docuclient.Facture', on_delete=models.CASCADE, blank = True, null = True, related_name='facture_client_administration')

    date_created = models.DateTimeField(auto_now_add = True)

    last_updated = models.DateTimeField(auto_now = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("adminstration-detail", kwargs = {"pk":self.pk})

    def __str__(self):

        return self.client_Name




""" 

########################################################################################################


            #    /***************** CLIENT CONVENTION ENTREPRISE DATA BASE ********************/
########################################################################################################



"""

class ConventionEntrepriseClient(models.Model):
    NATION = [
        ('National', 'National'),
        ('International', 'International'),
    ]

    nation_choices = models.CharField(choices = NATION, blank = True, null=True, max_length = 100)

    client_Name = models.CharField(null=True, blank=True, max_length=200)

    address = models.CharField(null=True, blank=True, max_length=255)

    postal_Code = models.CharField(null=True, blank=True, max_length=10)

    phone_number = PhoneNumberField()

    email_Address = models.EmailField(null=True, blank=True, max_length=200)

    partenary_code = models.CharField(max_length = 200, blank = True)

    taxe_TPS = models.FloatField(null=True, blank=True)

    taxe_CSS = models.FloatField(null=True, blank=True)

    remise = models.FloatField(null=True, blank=True)

    livraison = models.CharField(null=True, blank=True, max_length=200)

    modalite_paiement = models.FloatField(blank=True, null=True)

    devisconventionentrepriseClient = models.ForeignKey(DevisClient, on_delete = models.SET_NULL, null = True, blank = True, related_name = "devisconventionentrepriseClien")

    bonlivraison_convention_entreprise = models.ForeignKey(BonLivraison, on_delete = models.SET_NULL, null = True, blank = True, related_name = "bonlivraison_convention_entreprise")

    facture = models.ForeignKey('docuclient.Facture', on_delete=models.CASCADE, blank = True, null = True, related_name='facture_client_convention_entreprise')

    date_created = models.DateTimeField(auto_now_add = True)

    last_updated = models.DateTimeField(auto_now = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("client-convention-detail", kwargs = {"pk":self.pk})

    def __str__(self):

        return self.client_Name





""" 

########################################################################################################


             #   /***************** CLIENT ENTRAPRISE DATA BASE ********************/
########################################################################################################



"""

class EntrepriseClient(models.Model):

    NATION = [
        ('National', 'National'),
        ('International', 'International'),
    ]

    nation_choices = models.CharField(choices = NATION, blank = True, null=True, max_length = 100)

    client_Name = models.CharField(null=True, blank=True, max_length=200)

    address = models.CharField(null=True, blank=True, max_length=255)

    postal_Code = models.CharField(null=True, blank=True, max_length=10)

    phone_number = PhoneNumberField()

    email_Address = models.EmailField(null=True, blank=True, max_length=200)

    partenary_code = models.CharField(max_length = 200, blank = True, null=True)

    taxe_TPS = models.FloatField(null=True, blank=True)

    taxe_CSS = models.FloatField(null=True, blank=True)

    remise = models.FloatField(null=True, blank=True)

    livraison = models.CharField(null=True, blank=True, max_length=200)

    modalite_paiement = models.FloatField(blank=True, null=True)

    devisentrepriseClient = models.ForeignKey(DevisClient, on_delete = models.SET_NULL, null = True, blank = True, related_name = "devisentrepriseClient")

    bonlivraison_entreprise = models.ForeignKey(BonLivraison, on_delete = models.SET_NULL, null = True, blank = True, related_name = "bonlivraison_entreprise")

    facture = models.ForeignKey('docuclient.Facture', on_delete=models.CASCADE, blank = True, null = True, related_name='facture_client_entreprise')

    date_created = models.DateTimeField(auto_now_add = True)

    last_updated = models.DateTimeField(auto_now = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("entreprise-detail", kwargs = {"pk":self.pk})

    def __str__(self):

        return self.client_Name




""" 

########################################################################################################


               # /***************** ARTICLE DATA BASE ********************/
########################################################################################################



"""




class Articles(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)

    date_updated = models.DateTimeField(auto_now=True)

    model = models.CharField(max_length = 255, blank = False)

    name = models.CharField(max_length=255, blank = False)

    article_image = models.ImageField(upload_to='Articleimages/', blank = False)

    barcode = models.ImageField(upload_to='barcodeimages/', blank=True)

    article_id = models.CharField(max_length = 12, null=True)

    description = models.TextField(blank = False)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    active = models.BooleanField(default=False)

    price = models.FloatField(blank = False)

    stock = models.FloatField(blank=True, null=True)

    quantite_client = models.FloatField(blank=True, null=True)

    product = models.ForeignKey('alldetail.Product', on_delete=models.CASCADE, related_name='articles')

    likes = models.ManyToManyField(User, related_name='article_like')

    facture = models.ForeignKey(Facture, on_delete = models.SET_NULL, null = True, related_name = "facture_article")

    favouriteFacture = models.ForeignKey(Facture, on_delete = models.SET_NULL, null = True, related_name = "favouriteFacture")

    devisClientType = models.ForeignKey(DevisClient, on_delete = models.SET_NULL, null = True, blank = True, related_name = "devisClientType")

    bonlivraison = models.ForeignKey(BonLivraison, on_delete = models.SET_NULL, null = True, blank = True, related_name = "bonlivraison")

    def get_absolute_url(self):
        return reverse("articles-detail", kwargs = {"pk":self.pk})

    def number_of_likes(self):
        return self.likes.count()

    def name_of_article(self):
        return self.name.count()

    def __str__(self):
        return f'Article by {self.author.username} on {self.name}'

    def save(self, *args, **kwargs):

        EAN = barcode.get_barcode_class('ean13')

        ean = EAN(f'{self.article_id}{self.name}{self.model}', writer=ImageWriter())

        buffer = BytesIO()

        ean.write(buffer)

        self.barcode.save(f'{self.article_id}.png', File(buffer), save=False)

        return super().save(*args, **kwargs)

