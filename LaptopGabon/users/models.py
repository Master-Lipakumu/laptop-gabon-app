from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from alldetail.models import (Shop, Category, Product, Articles, ConventionEntrepriseClient,
EntrepriseClient, AdministrationClient, ClientParticulier)

from docuclient.models import ( Ravite, BonLivraison, Facture, DevisClient)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "profile_pics/", default="default.jpg", blank=True)
    articles = models.ManyToManyField(Articles)
    shops= models.ManyToManyField(Shop)
    categorys = models.ManyToManyField(Category)
    products = models.ManyToManyField(Product)
    conventionEntrepriseClients = models.ManyToManyField(ConventionEntrepriseClient)
    entrepriseClients = models.ManyToManyField(EntrepriseClient)
    administrationClients = models.ManyToManyField(AdministrationClient)
    clientParticuliers = models.ManyToManyField(ClientParticulier)
    ravites = models.ManyToManyField(Ravite)
    bonLivraisons = models.ManyToManyField(BonLivraison)
    factures = models.ManyToManyField(Facture)
    devisClients = models.ManyToManyField(DevisClient)
    is_staff = models.BooleanField(default = False)
    last_connect = models.DateTimeField(auto_now=True)