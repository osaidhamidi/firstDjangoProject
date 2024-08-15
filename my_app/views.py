from django.shortcuts import render


def index(request):
    return render(request, 'my_app/main.html')

def budgie_page(request):
    return render(request, 'my_app/pages/Budgie.html')

def canari_page(request):
    return render(request, 'my_app/pages/canari.html')

def cardinalred_page(request):
    return render(request, 'my_app/pages/cardinalred.html')

def coctail_page(request):
    return render(request, 'my_app/pages/coctail.html')
def cocatoo_page(request):
    return render(request, 'my_app/pages/cocatoo.html')


def goldenparakeet_page(request):
    return render(request, 'my_app/pages/goldenparakeet.html')

def grayparrot_page(request):
    return render(request, 'my_app/pages/grayparrot.html')

def home_page(request):
    return render(request, 'my_app/pages/home.html')

def lov_page(request):
    return render(request, 'my_app/pages/lov.html')

def macaw_page(request):
    return render(request, 'my_app/pages/macaw.html')

def ganna_page(request):
    return render(request, 'my_app/pages/ganna.html')

def siskin_page(request):
    return render(request, 'my_app/pages/siskin.html')

def turkman_page(request):
    return render(request, 'my_app/pages/turkman.html')

def yellowth_page(request):
    return render(request, 'my_app/pages/yellowth.html')

def zebra_page(request):
    return render(request, 'my_app/pages/zebra.html')