from django.db import models

# Create your models here.
class Favorite(models.Model):
    CHOICES = (
        ('Tarjeta', 'Tarjeta'),
        ('Manualidad', 'Manualidad'),
        ('Dibujo', 'Dibujo'),
        ('Pintura', 'Pintura'),
        ('Pintura en Tela', 'Pintura en Tela'),
    )
    
    title = models.CharField('Nombre:', max_length=60)
    category = models.CharField('Categoria:', choices=CHOICES, max_length=60, default='Tarjeta')
    image = models.ImageField('Imagen:', upload_to='photos', blank=False)
    is_available = models.BooleanField('Activo?',default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Favorito'   
        verbose_name_plural = 'Favoritos'
    
    def __str__(self):
        return self.title
    
    
class Contactame(models.Model):
    name = models.CharField('Nombre:', max_length=60)
    email = models.CharField('Correo:', max_length=100)
    phone = models.CharField('Telefono:', max_length=10)
    message = models.TextField('Mensaje:') 
    
    class Meta:
        verbose_name = 'Mensaje'   
        verbose_name_plural = 'Mensajes'
    
    def __str__(self):
        return self.name