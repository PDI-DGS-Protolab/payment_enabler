from django.shortcuts import render

def success(request):
    return render(request, 'success.html', {})

def pending(request):
    return render(request, 'pending.html', {})

def error(request):
    return render(request, 'error.html', {})