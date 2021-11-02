from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.conf import settings
from django.template.loader import template_source_loaders

__all__ = ['index', 'version', 'clear_template_cache']


def index(request):
    directory = settings.S3_TEMPLATE_LOADER_BUILD_DIRECTORY
    return render(request, "{}/index.html".format(directory))

def version(request):
    return JsonResponse({ version: settings.S3_TEMPLATE_LOADER_BUILD_DIRECTORY })

def clear_template_cache(request):
    if request.method != 'DELETE':
        return HttpResponseNotAllowed()
    if not template_source_loaders:
        return

    for loader in template_source_loaders:
        loader.reset()
    return HttpResponse(status=204)
