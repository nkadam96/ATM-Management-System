from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Account, Transaction
from django.contrib.auth import logout
from decimal import Decimal



def login_view(request):
    if request.method == "POST":
        card_number = request.POST.get("card")
        pin = request.POST.get("pin")

        try:
            user = Account.objects.get(card_number=card_number)

            if user.pin == pin:
                request.session["user_id"] = user.id
                return redirect("dashboard")
            else:
                return render(request, "error.html", {"message": "Invalid PIN"})

        except Account.DoesNotExist:
            return render(request, "error.html", {"message": "Card Number Not Found"})

    return render(request, "login.html")



def dashboard(request):
    if "user_id" not in request.session:
        return redirect("login")

    user = Account.objects.get(id=request.session["user_id"])
    return render(request, "dashboard.html", {"user": user})


def deposit(request):
    if "user_id" not in request.session:
        return redirect("login")

    user = Account.objects.get(id=request.session["user_id"])

    if request.method == "POST":
        amount = Decimal(request.POST.get("amount"))

        if amount <= 0:
            messages.error(request, "Enter a valid amount!")
            return redirect("deposit")

        user.balance += amount
        user.save()

        Transaction.objects.create(
            account=user,
            type="Deposit",
            amount=amount
        )

        messages.success(request, "Amount Deposited Successfully!")
        return redirect("dashboard")

    return render(request, "deposit.html")


def transfer(request):
    if "user_id" not in request.session:
        return redirect("login")

    sender = Account.objects.get(id=request.session["user_id"])

    if request.method == "POST":
        receiver_card = request.POST.get("card_number")
        amount = float(request.POST.get("amount"))

        try:
            receiver = Account.objects.get(card_number=receiver_card)
        except Account.DoesNotExist:
            messages.error(request, "Receiver Account Not Found")
            return redirect("transfer")

        if receiver.card_number == sender.card_number:
            messages.error(request, "You cannot transfer to your own account!")
            return redirect("transfer")

        if sender.balance < amount:
            messages.error(request, "Insufficient Balance!")
            return redirect("transfer")

        sender.balance -= amount
        receiver.balance += amount
        sender.save()
        receiver.save()

        Transaction.objects.create(account=sender, type="Transfer", amount=amount)
        Transaction.objects.create(account=receiver, type="Deposit", amount=amount)

        messages.success(request, "Transfer Successful!")
        return redirect("dashboard")

    return render(request, "transfer.html")


def mini_statement(request):
    if "user_id" not in request.session:
        return redirect("login")

    
    user = Account.objects.get(id=request.session["user_id"])

    
    transactions = Transaction.objects.filter(account=user).order_by('-timestamp')[:5]

    return render(request, "mini_statement.html", {
        "user": user,
        "transactions": transactions
    })

def withdraw(request):
    if "user_id" not in request.session:
        return redirect("login")

    user = Account.objects.get(id=request.session["user_id"])

    if request.method == "POST":
        amount = int(request.POST.get("amount"))

        if amount > user.balance:
            return render(request, "error.html", {"message": "Insufficient Balance!"})

        user.balance -= amount
        user.save()

        return redirect("success")

    return render(request, "withdraw.html")
def change_pin(request):
    if "user_id" not in request.session:
        return redirect("login")

    user = Account.objects.get(id=request.session["user_id"])

    if request.method == "POST":
        old_pin = request.POST.get("old_pin")
        new_pin = request.POST.get("new_pin")

        if user.pin != old_pin:
            return render(request, "error.html", {"message": "Old PIN is Incorrect!"})

        user.pin = new_pin
        user.save()

        return redirect("success")

    return render(request, "change_pin.html")
def logout_view(request):
    logout(request)
    return redirect('login')  
def home(request):
    return render(request, 'home.html')
def success_page(request):
    return render(request, "success.html")

