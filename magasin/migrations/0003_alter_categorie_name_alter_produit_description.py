# Generated by Django 4.1.7 on 2023-04-30 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0002_categorie_fournisseur_produitnc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='produit',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
