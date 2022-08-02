from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField

from django.urls import reverse

User = get_user_model()





########################################################################################################


              #  /***************** facture CLIENt DATA BASE ********************/
########################################################################################################


class Facture(models.Model):

    NATION = [
        ('National', 'National'),
        ('International', 'International'),
    ]

    TYPEPAYMENT = [
        ('A échéance','A échéance'),
        ('Définis dans le contrat','Définis dans le contrat'),
        ('Journalier, hebdomadaire, mensuel','Journalier, hebdomadaire, mensuel'),
    ]

    partenary_code = models.CharField(max_length = 200, blank = True, null=True)

    reduction_number = models.FloatField(blank = True, null=True)

    payment_modality = models.CharField(choices=TYPEPAYMENT, blank=True, null=True, max_length=200)

    modalite_paiement = models.FloatField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add = True)

    last_updated = models.DateTimeField(auto_now = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False )

    nation_choices = models.CharField(choices=NATION, blank=True, null=True, max_length=100)

    active = models.BooleanField(default=False)

    livraison = models.CharField(null=True, blank=True, max_length=200)

    date_created = models.DateTimeField(auto_now_add=True)

    date_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("facture-Detail", kwargs = {"pk":self.pk})

    def __str__(self):
        return f'document type {self.nation_choices}, crée le {self.date_created}'







""" 

########################################################################################################


                #/***************** Bon de livraison DATA BASE ********************/
########################################################################################################



"""


class BonLivraison(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)

    date_updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    client_name = models.CharField(max_length = 255)

    client_service = models.CharField(max_length = 255, blank = True, null = True)

    client_address = models.CharField(max_length = 300, blank = False)

    client_email = models.EmailField(blank = True, null = True)

    phone_number = PhoneNumberField()

    def get_absolute_url(self):
        return reverse("livraison-detail", kwargs = {"pk":self.pk})


    def __str__(self):
        return f"nom:{self.client_name},nom de l'article:{self.client_address},numero:{self.phone_number}"





""" 

########################################################################################################


              #  /***************** CLIENT TYPE DEVIS DATA BASE ********************/
########################################################################################################



"""

class DevisClient(models.Model):
    NATION = [
        ('National', 'National'),
        ('International', 'International'),
    ]

    TYPECLIENT = [
        ('Particuliers','Particuliers')
    ]

    TYPEPAYMENT = [
        ('A échéance','A échéance'),
        ('Définis dans le contrat','Définis dans le contrat'),
        ('Journalier, hebdomadaire, mensuel','Journalier, hebdomadaire, mensuel'),
    ]

    payment_modality = models.CharField(choices=TYPEPAYMENT, blank=True, null=True, max_length=200)

    nation_choices = models.CharField(choices=NATION, blank=True, null=True, max_length=100)

    client_type = models.CharField(choices=TYPECLIENT, blank=True, null=True, max_length=200)

    client_Name = models.CharField(null=True, blank=True, max_length=200)

    address = models.CharField(null=True, blank=True, max_length=255)

    postal_Code = models.CharField(null=True, blank=True, max_length=10)

    phone_number = PhoneNumberField()

    email_Address = models.EmailField(null=True, blank=True, max_length=200)

    taxe_TPS = models.FloatField(null=True, blank=True)

    taxe_CSS = models.FloatField(null=True, blank=True)

    livraison = models.CharField(null=True, blank=True, max_length=200)

    created = models.DateTimeField(auto_now_add = True)

    last_updated = models.DateTimeField(auto_now = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("devisclient-detail", kwargs = {"pk":self.pk})

    def __str__(self):
        return f'document type {self.nation_choices}, client type{self.client_type}'



""" 

########################################################################################################


              #  /***************** RAVITAILLEMENT DATA BASE ********************/
########################################################################################################



"""



class Ravite(models.Model):

    shop_name = models.CharField(blank = True, max_length = 255)
    
    article_name = models.CharField(blank = True, max_length = 255)

    article_number = models.IntegerField()

    article_description = models.TextField(blank = True)

    date_created = models.DateTimeField(auto_now_add=True)

    date_updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("ravite-detail", kwargs = {"pk":self.pk})


    def __str__(self):
        return f"nom de la boutique:{self.shop_name},nom de l'article:{self.article_name},nombre:{self.article_number}"
