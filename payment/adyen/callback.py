from py_adyen.adyen import Adyen

def callback(request):
    data = request.POST.dict()

    a = Adyen(data)

    if a.is_valid():
        print "VALID PAYMENT"