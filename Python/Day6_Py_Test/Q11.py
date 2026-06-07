# Create a custom exception `InsufficientFundsError`. Write standalone functions `deposit`, `withdraw`, `transfer` that operate on a dict representing an account. `withdraw` raises `InsufficientFundsError` for overdraft, `ValueError` for negative amounts, `TypeError` if amount isn't a number. Use try/except/finally to log every operation result.

class InsufficientFundsError(Exception):
    pass

class TransactionInteruppted(Exception):
    pass

def accountCheck():
    acc = int(input("Enter Account number to transect in: "))
    account = accounts.get(acc)

    if account:
        print(account)
        operations(amount, acc)
    else:
        print("Account not found")

def amountCheck(amount):
    try:
        amount = int(input("Enter amount: "))
    except ValueError:
        raise TypeError("Amount must be a number")
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    else:
        print("Valid Amount")
        return amount

def operations(amount, acc):
    print("Choose the operation: ")
    print("1. Deposit\n2. Withdraw\n3. Transfer\n4. Exit")
    choice = int(input())
    if choice == 1:
        try:
            deposit(amount, acc)
        except InsufficientFundsError as e:
            print(f"Operation failed: {e}")
        except ValueError as e:
            print(f"Invalid value: {e}")
        except TypeError as e:
            print(f"Invalid type: {e}")
        finally:
            print("Operation logged")
    elif choice == 2:
        try:
            withdraw(amount, acc)
        except InsufficientFundsError as e:
            print(f"Operation failed: {e}")
        except ValueError as e:
            print(f"Invalid value: {e}")
        except TypeError as e:
            print(f"Invalid type: {e}")
        finally:
            print("Operation logged")
    elif choice == 3:
        try:
            transfer(amount, acc)
        except InsufficientFundsError as e:
            print(f"Operation failed: {e}")
        except ValueError as e:
            print(f"Invalid value: {e}")
        except TypeError as e:
            print(f"Invalid type: {e}")
        finally:
            print("Operation logged")
    elif choice == 4:
        print(f"Balance: {accounts[acc]["Balance"]}")
        return accounts[acc]["Balance"]
    else:
        print("Invalid option")
        operations(amount, acc)

def deposit(amount, acc):
    amount = amountCheck(amount)
    accounts[acc]["Balance"] += amount
    print(f"Balance: {accounts[acc]["Balance"]}")
    return operations(amount, acc)

def withdraw(amount, acc):
    amount = amountCheck(amount)
    if amount > accounts[acc]["Balance"]:
        raise InsufficientFundsError("Insufficient Balance")
    else:
        accounts[acc]["Balance"] -= amount
        print(f"Balance: {accounts[acc]["Balance"]}")
        return operations(amount, acc)
    
def transfer(amount, acc):
    amount = amountCheck(amount)
    if amount > accounts[acc]["Balance"]:
        raise InsufficientFundsError("Insufficient Balance")
    else:
        transferAcc = int(input("Enter the Account Number to transfer the money too: "))
        accountAvail = accounts.get(transferAcc)

        if accountAvail:
            print(accountAvail)
            accounts[acc]["Balance"] -= amount
            print(f"Balance: {accounts[transferAcc]["Balance"]}")
            accounts[transferAcc]["Balance"] += amount
            print(f"Balance left after transfer: {accounts[acc]["Balance"]}")
            print(f"Balance of receiver account after recieving {amount}: {accounts[transferAcc]["Balance"]}")
        else:
            print("Account not found")

    
        return operations(amount, acc)

amount = 0

accounts = {
    12345: {
        "Name" : "Akash",
        "Balance" : 1000
    },

    54321: {
        "Name" : "Supan",
        "Balance" : 500
    }
}

try:
    accountCheck()
except TransactionInteruppted:
    print("Transaction Failed due to Interupption")
finally:
    print("Session Over")