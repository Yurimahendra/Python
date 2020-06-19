def rekursif(angka):
    if angka > 0 :
        print(angka)
        angka = angka - 2
        rekursif(angka)
    else:
        print("else",angka)
#masukan = int(input("masukan angka : "))
rekursif(3)
