from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def data_view(request):
    return render(request, 'data.html')

def test_view(request):
    return render(request, 'test.html')
