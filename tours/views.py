from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError
from django.views import View


def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request, departure: str):
    return render(request, 'tours/departure.html')


def tour_view(request, id: int):
    return render(request, 'tours/tour.html')

# class TestView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'test.html', {'name': 'Alex', 'place': 'Lab'})

def custom_handler400(request, exception):
    # Call when SuspiciousOperation raised
    return HttpResponseBadRequest('Неверный запрос!')


def custom_handler403(request, exception):
    # Call when PermissionDenied raised
    return HttpResponseForbidden('Доступ запрещен!')


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    # Call when raised some python exception
    return HttpResponseServerError('Ошибка сервера!')