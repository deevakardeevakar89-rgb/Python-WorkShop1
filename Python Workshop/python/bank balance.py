balance=10000
amount=int(input("Enter a amount : "))
if(amount>balance):
    print("you have insuffient balance")
else:
    print("Your amount has been debited")
    balance-=amount
    print(f"your new balance {balance}")
