import hashlib

plaintext = input("Nilai String : ")
sha = hashlib.sha1()

sha.update(plaintext.encode("ascii"))
print("nilai hash sha1 : ", sha.hexdigest())