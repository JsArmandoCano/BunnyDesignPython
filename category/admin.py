from django.contrib import admin
from .models import *
import admin_thumbnails

# Register your models here.

# Tarjetas
@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductsGallery
    extra = 1
    
class ProductTarjetaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]
    list_display = (
        'product_name',
        'slug',
        'category',
        'is_available',
        'created_date',
    )

admin.site.register(CategoryTarjeta)
admin.site.register(ProductTarjeta, ProductTarjetaAdmin)
admin.site.register(ProductsGallery)




# Manualidades
@admin_thumbnails.thumbnail('image')
class ProductGalleryInlineDos(admin.TabularInline):
    model = ProductsGalleryDos
    extra = 1

class ProductManualidadesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInlineDos]
    list_display = (
        'product_name',
        'slug',
        'category',
        'is_available',
        'created_date',
    )
    
admin.site.register(CategoryManualidades)
admin.site.register(ProductManualidades, ProductManualidadesAdmin)
admin.site.register(ProductsGalleryDos)




# Dibujos
@admin_thumbnails.thumbnail('image')
class ProductGalleryInlineTres(admin.TabularInline):
    model = ProductsGalleryTres
    extra = 1

class ProductDibyPinAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInlineTres]
    list_display = (
        'product_name',
        'slug',
        'category',
        'is_available',
        'created_date',
    )

admin.site.register(CategoryDibyPin)
admin.site.register(ProductDibyPin, ProductDibyPinAdmin)
admin.site.register(ProductsGalleryTres)




# Tela
@admin_thumbnails.thumbnail('image')
class ProductGalleryInlineCuatro(admin.TabularInline):
    model = ProductsGalleryCuatro
    extra = 1

class ProductTelaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInlineCuatro]
    list_display = (
        'product_name',
        'slug',
        'category',
        'is_available',
        'created_date',
    )

admin.site.register(CategoryTela)
admin.site.register(ProductTela, ProductTelaAdmin)
admin.site.register(ProductsGalleryCuatro)



# Comentarios
class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name',
        'rank',
        'is_available',
        'created_date',
    )

admin.site.register(Comments, CommentsAdmin)