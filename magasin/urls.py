import statistics
from django.conf import settings
from django.urls import include, path
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index, name='index'),

    path('home/', views.home, name='home'),
    path('register/',views.register, name = 'register'),
    path('magasin/search/', views.search, name='search'),
    path('magasin/<int:pk>/', views.product_detail, name='product_detail'),
    path('magasin/nouvFournisseur/',views.nouveauFournisseur,name='nouveauFour'),
    path('magasin/nouvProduit/',views.nouveauProduit,name='nouvProduit'),
    path('magasin/nouvProduitNC/',views.nouveauProduitNC,name='nouvProduitNC'),
    path('magasin/nouvCommande/',views.nouveauCommande,name='nouvCommande'),
    path('magasin/nouvCategorie/',views.nouveauCategorie,name='nouvCategorie') ,
    path('magasin/modifierFournisseur/<int:id>/',views.modifierFournisseur,name='modifierFournisseur'),
    path('magasin/modifierProduit/<int:id>/', views.modifierProduit, name='modifierProduit'),
    path('magasin/modifierProduitNC/<int:id>/',views.modifierProduitNC,name='modifierProduitNC'),
    path('magasin/modifierCommande/<int:id>/',views.modifierCommande,name='modifierCommande'),
    path('magasin/modifierCategorie/<int:id>/',views.modifierCategorie,name='modifierCategorie') ,
    path('magasin/supprimerFournisseur/<int:id>/',views.supprimerFournisseur,name='supprimerFournisseur'),
    path('magasin/supprimerProduit/<int:id>/',views.supprimerProduit,name='supprimerProduit'),
    path('magasin/supprimerProduitNC/<int:id>/',views.supprimerProduitNC,name='supprimerProduitNC'),
    path('magasin/supprimerCommande/<int:id>/',views.supprimerCommande,name='supprimerCommande'),
    path('magasin/supprimerCategorie/<int:id>/',views.supprimerCategorie,name='supprimerCategorie') ,
    path('accounts/', include('django.contrib.auth.urls')),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
