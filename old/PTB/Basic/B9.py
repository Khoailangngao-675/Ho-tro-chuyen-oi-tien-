A = [1,2,3,4,5,6]
#STT 0 1 2 3 4 5
#STT là số thứ tự
A[1] = 9
# A[1] = 9 là thay thế
A.sort()
#  sắp sếp danh sách 
A.append(8)
A.insert(2,4)  #Là thay thế số 3 trong A thành số 4
# 2 trong insert là số thứ thự của số cần thay thế 
# còn 4 là só thay thế cho 3
for i in range(len(A)):
    print(A[i])
