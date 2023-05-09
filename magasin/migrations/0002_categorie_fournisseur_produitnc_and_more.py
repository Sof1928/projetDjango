# Generated by Django 4.1.7 on 2023-03-07 09:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Alimentaire', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='ProduitNC',
            fields=[
                ('produit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='magasin.produit')),
                ('Duree_garantie', models.CharField(default=0, max_length=100)),
            ],
            bases=('magasin.produit',),
        ),
        migrations.RenameField(
            model_name='produit',
            old_name='libellé',
            new_name='libelle',
        ),
        migrations.AddField(
            model_name='produit',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='type',
            field=models.CharField(choices=[('em', 'emballé'), ('fr', 'Frais'), ('cs', 'Conserve')], default='em', max_length=2),
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCde', models.DateField(default=datetime.date.today, null=True)),
                ('totalCde', models.DecimalField(decimal_places=3, max_digits=10)),
                ('produits', models.ManyToManyField(to='magasin.produit')),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='Fournisseur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magasin.fournisseur'),
        ),
        migrations.AddField(
            model_name='produit',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magasin.categorie'),
        ),
    ]
