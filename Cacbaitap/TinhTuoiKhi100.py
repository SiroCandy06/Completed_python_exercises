import datetime

name = input("Nhập tên của bạn: ")
age = input("Nhập tuổi của bạn: ")
x = datetime.datetime.now()
year = x.year
year = int(year)
age = int(age)
age_100 = year + 100 - age

print("Name: " + name)
print("Năm khi mà bạn tròn 100 tuổi là: " + str(age_100) )


