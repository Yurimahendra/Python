from stegano import lsb

#gambar1 = input("gambar awal : ")
gambar2 = input("gambar yang akan berisi pesan : ")
#pesan = input("pesan rahasia : ")

#sembuntikan pesan
#secret = lsb.hide(gambar1, pesan)

#buat file gambar baru
#secret.save(gambar2)

#baca pesan rahasia
print(lsb.reveal(gambar2))