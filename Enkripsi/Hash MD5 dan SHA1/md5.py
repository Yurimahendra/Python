import hashlib

plainttext = input("nilai string : ")
md5 = hashlib.md5()
md5.update(plainttext.encode("ascii"))

print("Nilai hash md5 : ", md5.hexdigest())