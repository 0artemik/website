from django.shortcuts import render


def landing(request):
    """Одностраничный лендинг массажного салона."""
    return render(request, 'main/landing.html')
