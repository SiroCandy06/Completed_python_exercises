#Chương trình tìm ước số của 1 con số được input đầu vào
x = input("Enter The Numbers: ") # Dữ Liệu Người Dùng Nhập 

a = 0 
a = int(a)
x = int(x)
list = []
checking = []
while a <= x:
    a = a + 1
    numbers = a
    if x%numbers == 0:
        list.append(numbers) 
    elif x%numbers != 0:
        checking.append(numbers) # Cái checking tui thêm vào để check chương trình chạy. 
print("All divisors of the number you have given: ")
print(str(list))


