from django.views import View
from django.http import HttpResponse


class Test(View):
    def get(self, request):
        return HttpResponse('Hola mundo!!')


