from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import dbc, Transaction
from .forms import TransferForm
from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
# Create your views here.
from transfers.models import *
def test(request):
    return HttpResponse('testing the page')
def login(request):
    return render(request,'login.html')
def log(request):
    a=request.GET['email']
    b=request.GET['password']
    if dbc.objects.filter(email=a,pwd=b):
        # c=dbc.objects.get(email=a)
        return render(request,'home.html')#,#{'u':c})
    else:
        return render(request,'login.html')
# def index(request):
#     return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def input(request):
    m=dbc()
    m.Account_No=request.GET['account_no']
    m.CIF_No=request.GET['cif_no']
    m.email=request.GET['email']
    m.pwd=request.GET['password']   
    m.Branch_Code=request.GET['branch_code']
    m.Country=request.GET['country']
    m.Facility_Required=request.GET['facility_required']
    # m.Repeat_pwd=request.GET['password_repeat']
    m.gender=request.GET['gender']
    m.Registered_Mobile_No=request.GET['Registered_Mobile_No']
    m.save()
    return render(request,'welcome.html')
def Welcome(request):
    return render(request,'Welcome.html')
def home(request):
    return render(request,'home.html')
def aboutus(request):
    return render(request,'aboutus.html')

def accshow(request):
    u=dbc.objects.all()
    # u=user.objects.all()
    return render(request,'Account_info.html',{'u':u})
#     a=request.GET['email']
#     c=dbc.objects.get(email=a)
#     return render(request,'Account_info.html',{'u':c})
# def sinup()
# usecase

def adminlogin(request):
    return render(request,'adminlogin.html')
def adminapoorve(request):
    return render(request,'adminapoorve.html')

def adminlog(request):
    a=request.GET['user_id']
    b=request.GET['password']
    if dba.objects.filter(user_id=a,pwd=b):
        # c=dbc.objects.get(email=a)
        return render(request,'adminapoorve.html')#,#{'u':c})
    else:
        return render(request,'adminlogin.html')
def adminregister(request):
    return render(request,'adminregister.html')
def admininput(request):
    m=dba()
    m.user_id=request.GET['user_id']
    m.pwd=request.GET['password']  
    m.save()
    return render(request,'adminlogin.html')
def initial(request):
    return render(request,'initial.html')
def approve(request):
     a=request.GET['account_no']
     if dbc.objects.filter(Account_No=a):
        # c=dbc.objects.get(email=a)
        return render(request,'initial.html')#,#{'u':c})
     else:
        return render(request,'adminapoorve.html')
# def initialbalance(request):
#     m=dbc()
#     a=request.GET['accountNumber']
#     if dbc.objects.filter(Account_No=a):
#         m.balance=request.GET['amount']
#         m.save()
#         return render(request,'adminview.html')#,#{'u':c})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import dbc

def initialbalance(request):
    if request.method == 'POST':
        account_number = request.POST.get('accountNumber')
        initial_amount = request.POST.get('amount')

        if account_number and initial_amount:
            try:
                account = dbc.objects.get(Account_No=account_number)
                account.balance = int(initial_amount)
                account.save()
                return render(request,'adminview.html')
            except dbc.DoesNotExist:
                return HttpResponse("Account number not found.")
        else:
            return HttpResponse("Please provide both account number and initial amount.")

    return render(request, 'initialbalance.html')
def show(request):
    return render(request,'show.html')
def adminview(request):
    return render(request,'adminview.html')

def vieww(request):
    account_number = request.GET.get('account_number')
    phone = request.GET.get('phone')
    
    if account_number and phone:
        # Filter the dbc model for the specific account number and phone number
        user = dbc.objects.filter(Account_No=account_number, Registered_Mobile_No=phone).first()
        
        if user:
            # If user is found, pass it to the template
            return render(request, 'show.html', {'user': user})
        else:
            # If no user is found, you can pass an error message to the template
            return render(request, 'show.html', {'error': 'No user found with the provided account number and phone number.'})
    else:
        return render(request, 'adminview.html', {'error': 'Please provide both account number and phone number.'})

def transfer_funds(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            sender_account_no = form.cleaned_data['sender']
            receiver_account_no = form.cleaned_data['receiver']
            amount = form.cleaned_data['amount']
            tpin = form.cleaned_data['tpin']
            description = form.cleaned_data['description']

            try:
                sender = dbc.objects.get(Account_No=sender_account_no)
                receiver = dbc.objects.get(Account_No=receiver_account_no)
                
                # Verify TPIN
                if sender.pwd != tpin:  # Assuming 'pwd' is used as TPIN here
                    return HttpResponse("Invalid TPIN", status=403)

                if sender.transfer(amount, receiver):
                    Transaction.objects.create(
                        sender=sender,
                        receiver=receiver,
                        amount=amount,
                        tpin=tpin,
                        description=description
                    )
                    return HttpResponse("Transfer successful")
                else:
                    return HttpResponse("Insufficient balance", status=400)
            except dbc.DoesNotExist:
                return HttpResponse("Invalid account number", status=404)
    else:
        form = TransferForm()

    return render(request, 'transfer.html', {'form': form})

# Create your views here.
