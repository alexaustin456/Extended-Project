#Method of Gauss (x/lnx)
import math
import time
start = time.time()
x = int(input("What limit would you like to select?"))
piX = x/(math.log(x))
end = time.time()
print(pi(x) =, (piX))
print(end - start, "seconds")
#piX = int(round(piX,0))
#print "pi(x) =", (piX),"(To the nearest integer)"
