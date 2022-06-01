from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕 세상아. You're at the polls index.")
