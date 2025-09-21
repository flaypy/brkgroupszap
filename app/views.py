from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Group, Category
from django.db.models import F


# View para renderizar a página principal com os grupos
def group_list(request):
    """
    Busca todos os grupos no banco de dados, ordenados pelos mais recentes,
    e os envia para o template HTML.
    """
    groups = Group.objects.all().select_related('category').order_by('-created_at')

    # Busca todas as categorias para exibir na interface
    categories = Category.objects.all()

    context = {
        'groups': groups,
        'categories': categories
    }
    return render(request, 'index.html', context)


def redirect_and_count(request, group_id):
    """
    Incrementa a contagem de visualizações de um grupo e redireciona
    para o link do WhatsApp.
    """
    group = get_object_or_404(Group, pk=group_id)
    # Usamos F() para evitar condições de corrida e fazer o update no banco de dados
    group.views = F('views') + 1
    group.save(update_fields=['views'])
    return redirect(group.whatsapp_link)


# View de API para retornar os grupos em formato JSON (se necessário no futuro)
def group_list_api(request):
    """
    Retorna uma lista de todos os grupos em formato JSON.
    Isso permite que o frontend seja construído de forma dinâmica com JavaScript.
    """
    groups = Group.objects.values(
        'name',
        'description',
        'image_url',
        'whatsapp_link',
        'category__name',
        'views'
    )
    return JsonResponse(list(groups), safe=False)
