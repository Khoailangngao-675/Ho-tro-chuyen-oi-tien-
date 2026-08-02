ho_ten = input()
x = ho_ten.split(" ")
ho = x[0]
dem = " "
for i in range (1,len(x)-1) :
    dem = dem + " " + x[i]
ten = x[-1]
print("Họ:",ho,", Tên Đệm:",dem ,", Tên:",ten)