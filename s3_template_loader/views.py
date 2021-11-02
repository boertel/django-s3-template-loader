from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.conf import settings
from django.template.utils import get_app_template_dirs
from django.views.decorators.csrf import csrf_exempt

__all__ = ['index', 'version', 'clear_template_cache']


def index(request):
    directory = settings.S3_TEMPLATE_LOADER_BUILD_DIRECTORY
    return render(request, "{}/index.html".format(directory))

def version(request):
    return JsonResponse({ "version": settings.S3_TEMPLATE_LOADER_BUILD_DIRECTORY })

@csrf_exempt
def clear_template_cache(request):
    if request.method != 'DELETE':
        return HttpResponseNotAllowed()
    get_app_template_dirs.cache_clear()
    return HttpResponse(status=204)
