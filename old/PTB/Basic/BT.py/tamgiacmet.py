a = int(input())
b = int(input())
c = int(input())
if a + b < c or a + c < b or b + c < a:
    print("Khong phai tam giac")
elif a == b and a == c and b == c:
    print("Tam giac deu")
elif a == b or a == c or c == b:
    print("Tam giac can")
elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
    print("Tam giac vuong")
else:
    print("Tam giac thuong")