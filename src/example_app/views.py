from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
print('Hello from feature2')
print('Hello from feature1')
