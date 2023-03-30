#Chương trình tìm ước số của 1 con số được input đầu vào
x = input("Enter The Numbers: ") # Dữ Liệu Người Dùng Nhập 

a = 0 
a = int(a)
x = int(x)
list = []
checking = []
while (a <= x): # Sử Dụng Vòng Lặp While Lặp lại và check xem numbers có chia hết ko
    a = a + 1
    testnumbers = x/a
    if testnumbers%a == 0:
        list.append(testnumbers)
    elif testnumbers != 0:
        checking.append(testnumbers)
print("All divisors of the number you have given: ")
print(str(list))
print("checking: " + str(checking))

