from django.contrib import admin

# Register your models here.

from .models import (Category, Shop, Product, Articles, EntrepriseClient,
ConventionEntrepriseClient, AdministrationClient, ClientParticulier )



admin.site.register(Shop)

admin.site.register(Category)

admin.site.register(Product)

admin.site.register(Articles)

admin.site.register(EntrepriseClient)

admin.site.register(ConventionEntrepriseClient)

admin.site.register(AdministrationClient)

admin.site.register(ClientParticulier)