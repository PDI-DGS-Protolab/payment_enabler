from py_adyen.adyen import Adyen

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.shortcuts import render

import sys

def success(request):
    return render(request, 'success.html', {})

def pending(request):
    return render(request, 'pending.html', {})

def error(request):
    return render(request, 'error.html', {})

@csrf_exempt
def callback(request):
    
    if request.method == 'GET':
        print "COMPLETE THIS CODE. DEAL WITH ALL POSSIBLE STATES and redirecited accordingly!"
        return success(request)
    
    if request.method == 'POST': 
        print "POST"
        sys.stdout.flush()
        
        data = request.POST.dict()
        
        print "DICT"
        print data
        sys.stdout.flush()
    
        a = Adyen(data)
        
        print "Client"
        sys.stdout.flush()

        print "Parse data structure and store resutls in database!"
    
        if a.is_valid():
            print "VALID"
            sys.stdout.flush()
            return HttpResponse("[accepted]", mimetype="text/plain")
        else:
            print "ERROR"
            sys.stdout.flush()
            return HttpResponse("[error]", mimetype="text/plain")
    
    