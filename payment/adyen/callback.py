from py_adyen.adyen import Adyen

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.shortcuts import render

def success(request):
    return render(request, 'success.html', {})

def pending(request):
    return render(request, 'pending.html', {})

def error(request):
    return render(request, 'error.html', {})

@csrf_exempt
def callback(request):
    
    if request.method == 'GET':
        return success(request)
    
    if request.method == 'POST':      
        data = request.POST.dict()
    
        a = Adyen(data)
    
        if a.is_valid():
            return HttpResponse("accepted", mimetype="text/plain")
        else:
            return HttpResponse("error", mimetype="text/plain")
    
    