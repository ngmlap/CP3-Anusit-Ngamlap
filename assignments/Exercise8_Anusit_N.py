unInput = input("ชื่อผู้ใช้ : ")
pwInput = input("รหัสผ่าน : ")
item1 = "โค๊ก"
item2 = "เป็ปซี่"
item3 = "แฟนต้า"
item4 = "เอส"
price1 = 15
price2 = 17
price3 = 16
price4 = 14
if unInput == "user" and pwInput == "111":
    print("****** ร้านเครื่องดื่มท้ายซอย ยินดีต้อนรับ ******")
    print("1.", item1, "กระป๋องละ ", price1, "บาท")
    print("2.", item2, "กระป๋องละ ", price2, "บาท")
    print("3.", item3, "กระป๋องละ ", price3, "บาท")
    print("4.", item4, "กระป๋องละ ", price4, "บาท")
    itemInput = int(input("เลือกรายการเครื่องดื่ม(1-4) : "))
    if itemInput == 1:
        totalInput = int(input("ต้องการกี่กระป๋อง : "))
        totalPrice = price1*totalInput
        print("-----เครื่องดื่มที่สั่ง------")
        print(item1, totalInput, "กระป๋อง")
        print("รวมราคา", totalPrice, "บาท")
        print("---------------------")
    elif itemInput == 2:
        totalInput = int(input("ต้องการกระป๋อง : "))
        totalPrice = price2*totalInput
        print("-----เครื่องดื่มที่สั่ง------")
        print(item2, totalInput, "กระป๋อง")
        print("รวมราคา", totalPrice, "บาท")
        print("---------------------")
    elif itemInput == 3:
        totalInput = int(input("ต้องการกี่กระป๋อง : "))
        totalPrice = price3*totalInput
        print("-----เครื่องดื่มที่สั่ง------")
        print(item3, totalInput, "กระป๋อง")
        print("รวมราคา", totalPrice, "บาท")
        print("---------------------")
    elif itemInput == 4:
        totalInput = int(input("ต้องการกี่กระป๋อง : "))
        totalPrice = price4 * totalInput
        print("-----เครื่องดื่มที่สั่ง------")
        print(item4, totalInput, "กระป๋อง")
        print("รวมราคา", totalPrice, "บาท")
        print("---------------------")
    else:
        print("คูณไม่ได้เลือกรายการที่กำหนด!!")
else:
    print("ชื่อผู้ใช้หรือรหัสผ่านผิด!!")