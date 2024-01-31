from django.contrib import admin
from .models import *
# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display=('id','nome_produto')

class MaterialAdmin(admin.ModelAdmin):
    list_display=('id','name_material')

admin.site.register(Material, MaterialAdmin)
admin.site.register(Produto,ProdutoAdmin)