import math
import time
def sieve():
    x = int(input("What limit would you like to select?"))
    start = time.time()
    listX = list(range(3, x))
    listX.insert(0, 2)
    for i in range(2, x):
        a = 2
        while a <= x:
            if i*a in listX:
                listX.remove((i*a))
            a += 1
    end = time.time()
    print(listX)
    print(len(listX))#loop starts at 3 rather than zero
    print(end - start)
sieve()
