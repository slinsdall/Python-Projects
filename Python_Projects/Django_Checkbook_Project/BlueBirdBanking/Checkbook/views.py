from django.shortcuts import render, redirect
from .forms import AccountForm, TransactionForm

# This function will render the Home page when requested
def home(request):
    return render(request, 'checkbook/index.html')

# This function will render the Create New Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)  # Retrieve the account form
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # Check to see if the submitted form is valid and if so, saves it
            form.save()   # Saves new accounts
            return redirect('index')  # Returns user back to the home page
    content = {'form': form}  # Saves content to the template as a directory
    # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)

# This function will render the Balance page when requested
def balance(request):
    return render(request, 'checkbook/BalanceSheet.html')

# This function will render the Transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None)  # Retrieve the Transaction form
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # Checks to see if the submitted form is valid if so, it is saved
            form.save()  # Saves the transaction form
            return redirect('index')  # redirects user to the home page
        # Pass content to the template in a directory
        content = {'form': form}
        # Adds content of form to page
        return render(request, 'checkbook/AddTransaction.html', content)

