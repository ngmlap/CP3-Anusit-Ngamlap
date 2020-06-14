num = int(input("Please Enter Number : "))
for x in range(num,0,-1):
    y = "*"
    z = " "
    z = z * x
    print(z + (num-x) * y + y + (num-x) * y)

