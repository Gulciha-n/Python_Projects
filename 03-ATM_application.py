
BatuAccount = {
    'name' : 'Batu',
    'account no ' :'13245687',
    'amount' : 5000,
    'additional account':2000
    }

CansuAccount = {
    'name' : 'Cansu',
    'account no ' :'83245689',
    'amount' : 6000,
    'additional account':3000
    }

def withdraw(account,amount):
    print(f"Wellcome {account['name']} ")
    
    if account['amount'] >= amount:
        print("You can withdraw your money")
    else:
        total_amount = account['amount'] + account['additional account']
        if total_amount >= amount:
            print("Your account is not available do you want to use your additional account ?")
            answer = input("Please write yes or no : ")
            if (answer == 'yes'):
                print("Please withdraw your money")
            else:
                print("you have {account['amount']}$ in account no : {account['account no']}")
        else:
            print("insufficient balance")


withdraw(BatuAccount, 3000)
withdraw(BatuAccount, 6000)

withdraw(CansuAccount, 7000)
withdraw(CansuAccount, 10000)
   



