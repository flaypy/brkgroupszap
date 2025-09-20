from django.contrib import admin
from .models import Category, Group

# Customização da exibição dos Grupos na área de admin
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at', 'views')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    list_per_page = 25

# Registro simples do modelo de Categoria
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
