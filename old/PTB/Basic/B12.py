def gia_tri_tuyet_doi(n) :
    if n < 0:
        return-n
    else:
        return n
so_nhap = int(input("hay nhap mot so ngyen"))
n= so_nhap
ket_qua = gia_tri_tuyet_doi(n)
print("gia tri tuyet doi la", ket_qua)