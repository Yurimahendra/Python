print("perhitungan pajak")
print("-----------------")

penghasilan = int(input("Penghasilan kena pajak = "))

#tentukan pajak
if penghasilan > 500000000 :
    pajak = 2500000 + 15000000 + 87500000 + (penghasilan - 500000000) * 30 / 100
elif penghasilan > 150000000 :
    pajak = 2500000 + 15000000 + (penghasilan - 150000000) * 25 /100
elif penghasilan > 50000000 :
    pajak = 2500000 + (penghasilan - 50000000) * 15 / 100
else:
   pajak = penghasilan * 5 / 100


#tampilkan hasilnya
print("pajak = ", int(pajak))