from django.shortcuts import render

def billing(request):
    return render(request, 'billing/billing.html')
