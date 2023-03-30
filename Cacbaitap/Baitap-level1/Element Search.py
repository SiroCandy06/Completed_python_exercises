def binary_search(arr, low, high, x):
    #Trường hợp cơ sở
    if high >= low:
        mid = (high + low) // 2
        #Nếu phần tử có tồn tại ở phần giữa của mảng
        if arr[mid] == x:
            return mid
        #Nếu phần tử nhỏ hơn mid, nó sẽ nằm ở phía bên trái của mảng điểm gốc là tử phần tử mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        #Nếu không, phần tử sẽ nằm bên phải
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        #Phần tử không tồn tại trong tập hợp
        return -1

#Khởi tạo tập hợp
arr = [ 2, 3, 4, 8, 10 ]
x = 10
f = False
t = True


#Gọi hàm
result = binary_search(arr, 0, len(arr)-1, x)
if result != -1:
    print(t)
    print("có nằm trong danh sách hàm list")
else:
    print(f)
    print("ko nằm trong danh sách hàm list")
    
    
    

