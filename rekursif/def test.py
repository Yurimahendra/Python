def test(i,j):
    if(i == 0):
        return j
    else:
        print("i =", i, end=" ")
        print("J =",j,  )
        return test(i-1, i+j )

print(test(4, 7))