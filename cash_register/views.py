from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import OrdersForm

def mainMenu(request):
    if  request.method == 'POST':
        return redirect('scanItems')
    return render(request, 'mainMenu.html')

def scanItems(request):
    items = Items.objects.all()
    order = Orders.objects.get(id=1)

    found = False

    check = list(Orders.objects.filter(id=1))
    instance = get_object_or_404(Orders, id=1)
    form = OrdersForm(request.POST  or None, instance=instance)

    if (check):
        if  request.method == 'POST':
            print(request.POST)

            if 'cancel' in request.POST:
                form.instance.itemCode = ''
                form.instance.itemName = ''
                form.instance.itemPrice = ''
                form.instance.totalPrice = 0.0

                if form.is_valid():
                    form.save()

                return redirect('mainMenu')

            elif 'pay' in request.POST:
                receipt = order.itemPrice.split(' ')
                receipt2 = order.itemName.split(' ')
                total = order.totalPrice
                    
                context = {
                    'total': total,
                    'receipt': receipt,
                    'receipt2': receipt2,
                }

                return redirect('payment')

            elif 'scanner' in request.POST:
                scannedInput = request.POST['scanner']

                for item in items:

                    if(scannedInput == item.itemCode):
                        found = True

                        form.instance.itemCode += ' ' + item.itemCode
                        form.instance.itemName += ' ' + item.itemName
                        form.instance.itemPrice += ' ' + str(item.itemPrice)
                        form.instance.totalPrice += item.itemPrice

                        receipt = order.itemPrice.split(' ')
                        receipt2 = order.itemName.split(' ')


                        if form.is_valid():
                            form.save()

                        context = {
                            'scannedInput': item.itemPrice,
                            'name': item.itemName,
                            'receipt': receipt,
                            'receipt2': receipt2,
                        }

                        return render(request, 'scanItems.html', context)

            if not found:
                receipt = order.itemPrice.split(' ')
                receipt2 = order.itemName.split(' ')
                    
                context = {
                        'name': 'Incorrect Barcode!',
                        'receipt': receipt,
                        'receipt2': receipt2,
                    }

                return render(request, 'scanItems.html', context)

    return render(request, 'scanItems.html', {'scannedInput': ''})

def payment(request):
    check = list(Orders.objects.filter(id=1))
    instance = get_object_or_404(Orders, id=1)
    form = OrdersForm(request.POST  or None, instance=instance)

    order = Orders.objects.get(id=1)

    receipt = order.itemPrice.split(' ')
    receipt2 = order.itemName.split(' ')
    total = order.totalPrice

    if (check):
        if  request.method == 'POST':
            form.instance.itemCode = ''
            form.instance.itemName = ''
            form.instance.itemPrice = ''
            form.instance.totalPrice = 0.0   
            
            if form.is_valid():
                form.save()

            if 'cancel' in request.POST:
                return redirect('mainMenu')

            elif 'Debit' in request.POST:
                paymentType = request.POST['Debit']
                return render(request, 'thankyou.html', { 'type' : paymentType })

            elif 'Credit' in request.POST:
                paymentType = request.POST['Credit']
                return render(request, 'thankyou.html', { 'type' : paymentType })

            elif 'Cash' in request.POST:
                paymentType = request.POST['Cash']
                return render(request, 'thankyou.html', { 'type' : paymentType })
            elif 'end' in request.POST:
                return redirect('mainMenu')
         
    context = {
        'total': total,
        'receipt': receipt,
        'receipt2': receipt2,
    }
    
    return render(request, 'payment.html', context)