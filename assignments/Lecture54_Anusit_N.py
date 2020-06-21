def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        showMenu()
    else:
        print("Error : Invalid Username or Password")
        login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()

def menuSelect():
    userSelected = int(input("Select Menu>>"))
    if userSelected==1:
       totalPrice=(int(input("Total Price: ")))
       vatCalculator(totalPrice)
    elif userSelected==2:
        priceCalculator()
    else:
        print("Error : Please Select Menu")
        menuSelect()
    #return userSelected

def vatCalculator(totalPrice):
    vat = 7
    vatPrice = totalPrice + (totalPrice * vat / 100)
    # result
    print("vatCalculator = ",vatPrice)
    print("---End Program---")
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)
    print("---End Program---")

print(login())

