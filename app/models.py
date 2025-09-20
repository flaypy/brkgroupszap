from django.db import models


# Modelo para as categorias dos grupos
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['name']

    def __str__(self):
        return self.name


# Modelo para os grupos de WhatsApp
class Group(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome do Grupo")
    description = models.TextField(verbose_name="Descrição", help_text="Uma breve descrição sobre o que é o grupo.")
    image_url = models.URLField(max_length=500, verbose_name="URL da Imagem (Ícone)",
                                help_text="Link para uma imagem quadrada (ex: 200x200).")
    whatsapp_link = models.URLField(max_length=500, unique=True, verbose_name="Link de Convite do Grupo")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="groups",
        verbose_name="Categoria"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    views = models.PositiveIntegerField(default=0, verbose_name="Visualizações", editable=False)

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

