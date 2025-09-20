from django.shortcuts import render
from django.http import JsonResponse
from .models import Group

# View para renderizar a página principal com os grupos
def group_list(request):
    """
    Busca todos os grupos no banco de dados e os envia para o template HTML.
    """
    groups = Group.objects.all().select_related('category')
    return render(request, 'app/index.html', {'groups': groups})

# View de API para retornar os grupos em formato JSON (uma abordagem mais moderna)
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
