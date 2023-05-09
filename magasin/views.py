from django.shortcuts import get_object_or_404, render 
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect



# Create your views here.


def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home.html')
    else :
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form' : form})


def nouveauProduit(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            products= Produit.objects.all()
            context={'products':products}
            return render( request,'magasin/mesProduits.html ',context )
    else:
        form = ProduitForm()  # créer formulaire vide
    return render(request, 'magasin/majProduits.html', {'form': form})

def modifierProduit(request, id):
    post = get_object_or_404(Produit, id=id)

    if request.method == 'GET':
        context = {'form': ProduitForm(instance=post), 'id': id}
        return render(request,'magasin/modifierProduit.html',context)
    elif request.method == 'POST':
        form = ProduitForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            products= Produit.objects.all()
            context={'products':products}
            return render( request,'magasin/mesProduits.html ',context )
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'magasin/modifierProduit.html',{'form':form})

def supprimerProduit(request, id):
    produit = get_object_or_404(Produit, id=id)
    produit.delete()
    products = Produit.objects.all()
    context = {'products': products}
    return render(request, 'magasin/mesProduits.html', context)
         

   

def nouveauFournisseur(request):
    if request.method=="POST":
        form=FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            fournisseurs= Fournisseur.objects.all()
            context={'fournisseurs':fournisseurs}
            return render( request,'magasin/mesFournisseurs.html ',context )
    else:
        form=FournisseurForm()
    return render(request,'magasin/fournisseur.html',{'form':form})

def modifierFournisseur(request, id):
    post = get_object_or_404(Fournisseur, id=id)

    if request.method == 'GET':
        context = {'form': FournisseurForm(instance=post), 'id': id}
        return render(request,'magasin/modifierFournisseur.html',context)
    elif request.method == 'POST':
        form = FournisseurForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            fournisseurs= Fournisseur.objects.all()
            context={'fournisseurs':fournisseurs}
            return render( request,'magasin/mesFournisseurs.html ',context )
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'magasin/modifierFournisseur.html',{'form':form})

def supprimerFournisseur(request, id):
    fournisseur = get_object_or_404(Fournisseur, id=id)
    fournisseur.delete()
    fournisseurs= Fournisseur.objects.all()
    context={'fournisseurs':fournisseurs}
    return render( request,'magasin/mesFournisseurs.html ',context )
         

   
def nouveauCategorie(request):
    if request.method=="POST":
        form=CategorieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            categories= Categorie.objects.all()
            context={'categories':categories}
            return render( request,'magasin/mesCategorie.html ',context )   
    else:
        form=CategorieForm()
    return render(request,'magasin/categorie.html',{'form':form})

def modifierCategorie(request, id):
    post = get_object_or_404(Categorie, id=id)
    if request.method == 'GET':
        context = {'form': CategorieForm(instance=post), 'id': id}
        return render(request,'magasin/modifierCategorie.html',context)
    elif request.method == 'POST':
        form = CategorieForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            categories= Categorie.objects.all()
            context={'categories':categories}
            return render( request,'magasin/mesCategorie.html ',context )
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'magasin/modifierCategorie.html',{'form':form})

def supprimerCategorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    categorie.delete()
    categories= Categorie.objects.all()
    context={'categories':categories}
    return render( request,'magasin/mesCategorie.html ',context )
         
def nouveauCommande(request):
    if request.method=="POST":
        form=CommandeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            commandes= Commande.objects.all()
            context={'commandes':commandes}
            return render( request,'magasin/mesCommandes.html ',context )   
    else:
        form=CommandeForm()
    return render(request,'magasin/commande.html',{'form':form})

def modifierCommande(request, id):
    post = get_object_or_404(Commande, id=id)

    if request.method == 'GET':
        context = {'form': CommandeForm(instance=post), 'id': id}
        return render(request,'magasin/modifierCommande.html',context)
    elif request.method == 'POST':
        form = CommandeForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            commandes= Commande.objects.all()
            context={'commandes':commandes}
            return render( request,'magasin/mesCommandes.html ',context )
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'magasin/modifierCommande.html',{'form':form})

def supprimerCommande(request, id):
    commande = get_object_or_404(Commande, id=id)
    commande.delete()
    commandes= Commande.objects.all()
    context={'commandes':commandes}
    return render( request,'magasin/mesCommandes.html ',context )

def nouveauProduitNC(request):
    if request.method=="POST":
        form=ProduitNCForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            produitsNC=ProduitNC.objects.all()
            context={'produitsNC':produitsNC}
            return render( request,'magasin/mesProduitsNC.html ',context )  
    else:
        form=ProduitNCForm()
    return render(request,'magasin/produitNC.html',{'form':form})


def modifierProduitNC(request, id):
    post = get_object_or_404(ProduitNC, id=id)
    if request.method == 'GET':
        context = {'form': ProduitNCForm(instance=post), 'id': id}
        return render(request,'magasin/modifierProduitNC.html',context)
    elif request.method == 'POST':
        form = ProduitForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            produitsNC= Produit.objects.all()
            context={'produitsNC':produitsNC}
            return render( request,'magasin/mesProduitsNC.html ',context )
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'magasin/modifierProduitNC.html',{'form':form})

def supprimerProduitNC(request, id):
    produitNC = get_object_or_404(ProduitNC, id=id)
    produitNC.delete()
    produitsNC = ProduitNC.objects.all()
    context = {'produitsNC': produitsNC}
    return render(request, 'magasin/mesProduits.html', context)
         


def index(request):
    return render(request,'acceuil.html' )


def search(request):
    query = request.GET.get('q')
    if query:
        produits = Produit.objects.filter(libelle__icontains=query)
        context = {'query': query, 'produits': produits}
        return render(request, 'magasin/search_results.html', context)
    else:
        return render(request, 'magasin/search_results.html')
    
def product_detail(request, pk):
    product = get_object_or_404(Produit, pk=pk)
    return render(request, 'magasin/detail_product.html', {'product': product})

@login_required
def home(request):
    context={'val':"Menu Acceuil"}
    return render(request,'home.html',context)
