from distutils.command import upload
from unittest.util import _MAX_LENGTH
from django.urls import reverse 
from django.db import models

# Create your models here.

# Modelos para tarjeta
class CategoryTarjeta(models.Model):
    category = models.CharField('Categoria:', max_length=50, blank=False)
    icon = models.CharField('Icono:', max_length=100, blank=False)
    is_available = models.BooleanField('Activo?',default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Categoria de Tarjeta'   
        verbose_name_plural = 'Categorias de Tarjetas'
        
    def get_url(self):
        return reverse('products_by_category_tarjeta', args=[self.category])
    
    def __str__(self):
        return self.category
    
    
class ProductTarjeta(models.Model):
    product_name = models.CharField('Nombre:', max_length=100, blank=False)
    slug = models.CharField('Slug:', max_length=100)
    description = models.TextField('Descripcion:', max_length=200)
    img = models.ImageField('Imagen:', upload_to='photos/products', blank=False)
    category = models.ForeignKey(CategoryTarjeta, on_delete=models.CASCADE)
    is_available = models.BooleanField('Activo?',default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Producto Tarjeta'   
        verbose_name_plural = 'Productos de Tarjetas'
        
    def get_url_new(self):
        return reverse('detail_tarjeta', args=[self.category.category, self.slug])
    
    def __str__(self):
        return self.product_name
    

class ProductsGallery(models.Model):
    product = models.ForeignKey(ProductTarjeta, default=None, on_delete=models.CASCADE)
    image = models.ImageField('Imagen', upload_to='photos/products')
    
    class Meta:
        verbose_name = 'Mas Imagenes Tarjeta'   
        verbose_name_plural = 'Mas Imagenes Tarjetas'
    
    def __str__(self):
        return self.product.product_name
    
    
# Modelos para Manualidades
class CategoryManualidades(models.Model):
    category = models.CharField('Categoria:', max_length=50, blank=False)
    icon = models.CharField('Icono:', max_length=100, blank=False)
    is_available = models.BooleanField('Activo?',default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Categoria de Manualidad'   
        verbose_name_plural = 'Categorias de Manualidades'
        
    def get_url(self):
        return reverse('products_by_category_manualidad', args=[self.category])
    
    def __str__(self):
        return self.category
    
    
class ProductManualidades(models.Model):
    product_name = models.CharField('Nombre:', max_length=100, blank=False)
    slug = models.CharField('Slug:', max_length=100)
    description = models.TextField('Descripcion:', max_length=200)
    img = models.ImageField('Imagen:', upload_to='photos/products', blank=False)
    category = models.ForeignKey(CategoryManualidades, on_delete=models.CASCADE)
    is_available = models.BooleanField('Activo?',default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Producto Manualidad'   
        verbose_name_plural = 'Productos de Manualidades'
        
    def get_url_new(self):
        return reverse('detail_manu', args=[self.category.category, self.slug])
    
    def __str__(self):
        return self.product_name
    

class ProductsGalleryDos(models.Model):
    product = models.ForeignKey(ProductManualidades, default=None, on_delete=models.CASCADE)
    image = models.ImageField('Imagen', upload_to='photos/products')
    
    class Meta:
        verbose_name = 'Mas Imagenes Manualidad'   
        verbose_name_plural = 'Mas Imagenes Manualidades'
    
    def __str__(self):
        return self.product.product_name
    
    
# Modelos pa Pinturas y Dibujos    
class CategoryDibyPin(models.Model):
    category = models.CharField('Categoria:', max_length=50, blank=False)
    icon = models.CharField('Icono:', max_length=100, blank=False)
    is_available = models.BooleanField('Activo?',default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Categoria de Dibujo'   
        verbose_name_plural = 'Categorias de Dibujos'
        
    def get_url(self):
        return reverse('products_by_category_dibypins', args=[self.category])
    
    def __str__(self):
        return self.category
    
    
class ProductDibyPin(models.Model):
    product_name = models.CharField('Nombre:', max_length=100, blank=False)
    slug = models.CharField('Slug:', max_length=100)
    description = models.TextField('Descripcion:', max_length=200)
    img = models.ImageField('Imagen:', upload_to='photos/products', blank=False)
    category = models.ForeignKey(CategoryDibyPin, on_delete=models.CASCADE)
    is_available = models.BooleanField('Activo?',default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Producto Dibujo'   
        verbose_name_plural = 'Productos de Dibujos'
        
    def get_url_new(self):
        return reverse('detail_dibypin', args=[self.category.category, self.slug])
    
    def __str__(self):
        return self.product_name
    

class ProductsGalleryTres(models.Model):
    product = models.ForeignKey(ProductDibyPin, default=None, on_delete=models.CASCADE)
    image = models.ImageField('Imagen', upload_to='photos/products')
    
    class Meta:
        verbose_name = 'Mas Imagenes Dibujo'   
        verbose_name_plural = 'Mas Imagenes Dibujos'
    
    def __str__(self):
        return self.product.product_name
    
    
# Modelos para Pintura en Tel   
class CategoryTela(models.Model):
    category = models.CharField('Categoria:', max_length=50, blank=False)
    icon = models.CharField('Icono:', max_length=100, blank=False)
    is_available = models.BooleanField('Activo?',default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Categoria de Tela'   
        verbose_name_plural = 'Categorias de Telas'
        
    def get_url(self):
        return reverse('products_by_category_tela', args=[self.category])
    
    def __str__(self):
        return self.category
    
    
class ProductTela(models.Model):
    product_name = models.CharField('Nombre:', max_length=100, blank=False)
    slug = models.CharField('Slug:', max_length=100)
    description = models.TextField('Descripcion:', max_length=200)
    img = models.ImageField('Imagen:', upload_to='photos/products', blank=False)
    category = models.ForeignKey(CategoryTela, on_delete=models.CASCADE)
    is_available = models.BooleanField('Activo?',default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Producto Tela'   
        verbose_name_plural = 'Productos de Telas'
        
    def get_url_new(self):
        return reverse('detail_tela', args=[self.category.category, self.slug])
    
    def __str__(self):
        return self.product_name
    
    
class ProductsGalleryCuatro(models.Model):
    product = models.ForeignKey(ProductTela, default=None, on_delete=models.CASCADE)
    image = models.ImageField('Imagen', upload_to='photos/products')
    
    class Meta:
        verbose_name = 'Mas Imagenes Tela'   
        verbose_name_plural = 'Mas Imagenes Telas'
    
    def __str__(self):
        return self.product.product_name
    
    
    
# Comentarios
class Comments(models.Model):
    name = models.CharField('Nombre', max_length=60, blank=False)
    last_name = models.CharField('Apellidos', max_length=60, blank=False)
    rank = models.IntegerField('Calificación', blank=False)
    description = models.TextField('Descripción:', max_length=200)
    is_available = models.BooleanField('Activo?',default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Comentario'   
        verbose_name_plural = 'Comentarios'
    
    def __str__(self):
        return self.name