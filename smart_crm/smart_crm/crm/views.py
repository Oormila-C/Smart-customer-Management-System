from django.shortcuts import render, redirect
from .models import Customer

def home(request):
    return render(request, 'home.html')

def add_customer(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        company = request.POST['company']
        address = request.POST['address']

        Customer.objects.create(
            name=name,
            phone=phone,
            email=email,
            company=company,
            address=address
        )
        return redirect('customer_list')

    return render(request, 'add_customer.html')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})
from .models import Lead

def add_lead(request):
    customers = Customer.objects.all()
    if request.method == 'POST':
        customer_id = request.POST['customer']
        status = request.POST['status']
        follow_up = request.POST['follow_up']
        notes = request.POST['notes']

        customer = Customer.objects.get(id=customer_id)
        Lead.objects.create(
            customer=customer,
            status=status,
            follow_up_date=follow_up,
            notes=notes
        )
        return redirect('lead_list')

    return render(request, 'add_lead.html', {'customers': customers})


def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'lead_list.html', {'leads': leads})
def dashboard(request):
    total_customers = Customer.objects.count()
    total_leads = Lead.objects.count()
    converted = Lead.objects.filter(status="Converted").count()
    pending = Lead.objects.exclude(status="Converted").count()

    return render(request, 'dashboard.html', {
        'total_customers': total_customers,
        'total_leads': total_leads,
        'converted': converted,
        'pending': pending
    })
