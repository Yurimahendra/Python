while True:
    try:
        bil = input("masukan bilangan: ")
        bil = int(bil)
        break
    except ValueError:
        print("anda salah memasukan bilangan")
    print("anda memasukan bilangan %s, data harus angka" % bil )
print("anda memasukan bilangan", bil)