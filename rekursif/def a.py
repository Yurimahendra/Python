def a(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        #print(" ini n-1 " , a(n-1))
        #print("ini n-2 ",a(n-2))
        #print("ini return")
        return a(n-1)+a(n-2)

for i in range(0,4):
    print(a(i), end=" ")

