# Generated by Django 4.1 on 2022-08-22 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_productsgallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productsgallery',
            options={'verbose_name': 'Mas Imagenes Tarjeta', 'verbose_name_plural': 'Mas Imagenes Tarjetas'},
        ),
        migrations.CreateModel(
            name='ProductsGalleryTres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/products', verbose_name='Imagen')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='category.productdibypin')),
            ],
            options={
                'verbose_name': 'Mas Imagenes Dibujo',
                'verbose_name_plural': 'Mas Imagenes Dibujos',
            },
        ),
        migrations.CreateModel(
            name='ProductsGalleryDos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/products', verbose_name='Imagen')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='category.productmanualidades')),
            ],
            options={
                'verbose_name': 'Mas Imagenes Manualidad',
                'verbose_name_plural': 'Mas Imagenes Manualidades',
            },
        ),
        migrations.CreateModel(
            name='ProductsGalleryCuatro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/products', verbose_name='Imagen')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='category.producttela')),
            ],
            options={
                'verbose_name': 'Mas Imagenes Tela',
                'verbose_name_plural': 'Mas Imagenes Telas',
            },
        ),
    ]
