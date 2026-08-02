n = input("số điểm bạn đã có ")
nn=n.split(" ")
soluong10 = 0
i= 0
for i in nn :
    if i == "10":
        #
        soluong10=+1
        if soluong10 == 0 :
            print("Bạn không có điểm 10")
        else :
            print("Số lượng điểm 10 của bạn là", soluong10 )