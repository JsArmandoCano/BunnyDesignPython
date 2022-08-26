from django.contrib import admin
from .models import Favorite, Contactame

# Register your models here.
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
    )
    
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
    )

admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Contactame, ContactAdmin)