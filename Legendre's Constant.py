#Legendre's constant
import math
import time
x = int(input("What limit would you like to select?"))
start = time.time()
piX = x/(math.log(x)-1.08366)
end = time.time()
print(piX)
print(end - start)






