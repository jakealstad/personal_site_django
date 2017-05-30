from django.shortcuts import render


def home(request):
    return render(request, 'calling_card/home.html', {
        'page_title': 'Home',
        })


def resume(request):
    return render(request, 'calling_card/resume.html', {
        'page_title': 'Résumé',
        })
