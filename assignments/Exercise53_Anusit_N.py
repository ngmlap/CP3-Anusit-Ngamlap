def vtCaaculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
totalPrice=float(input("Input Price"))
print("Total Price = ",vtCaaculate(totalPrice))