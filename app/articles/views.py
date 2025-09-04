from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def list_articles(request):
    return JsonResponse({"message": "voici tous mes articles"})
