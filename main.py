bal=10000

p=int(input("Enter your password:"))
password=2725

def withdraw():
    global bal
    wt= int(input("Enter the amount:"))
    if (wt<= bal):
        bal-=wt
        print("Your Account balance is :",bal)
        print("Thank you!")
        return bal

    else:
        print("Insufficient  Acccount Balance!")


def deposit():
    global bal
    dp= int(input("Enter the deposit Amount:"))
    bal+=dp
    print("Your Account Balance is:", bal)
    return bal
    print("Thank you!")

def statement():
    global bal
    print("Your current account balance is :", bal)
    print("Thank you!")

while True:
    if (p== password):
        ope = input(" Select the operation:"
                    "1.CASH WITHDRAW (a),"
                    "2.CASH DEPOSIT (b),"
                    "3.STATEMENT (c),"
                    "4.CANCLE"
                    )
        if (ope=="a"):
            withdraw()

        elif(ope=="b"):
            deposit()
        elif(ope=="c"):
           statement()

        elif(ope=="d"):
            print("Thank you for use this ATM, Have a nice day!")
            break

        else:
            print("Select a proper operation")


    else:
        print("Wrong Password!")
        break
