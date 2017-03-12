from django.http import *


def first_page(request):
    return HttpResponse('<p>hello world </p>')