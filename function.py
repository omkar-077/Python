

# ****** FUNCTION EXAMPLE *****

wallet_balance = 50000

def add (balance):
    Value_toadd =int(input("Enter Amount to add :"))
    balance+= Value_toadd
    print(balance)
    return balance

def withdraw(balance):
    Value_toWithdraw = int(input("Enter amount to Withdraw :"))
    balance-= Value_toWithdraw
    print(balance)
    return balance

def checkBalance(balance):
    print(balance)
    return balance

while True :
    print("****Menu****")
    print("1.Add Amount")
    print("2. Withdraw Amt")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter Choice :").lower()
    if choice == '1' or choice =='add':
        wallet_balance = add(wallet_balance)

    elif choice =='2' or choice == 'withdraw':
        wallet_balance = withdraw(wallet_balance)
    elif choice == '3' or choice == 'checkbalance':
        wallet_balance =checkBalance(wallet_balance)
    elif choice == '4' or choice == 'exit':
        break
    else :
        print("Invalid input")