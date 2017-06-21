import math
i = 0
a = 0.1
x = 0.1
y = 0.1
for i in range(500): 
    fxy = math.exp(math.sin(x)+math.sin(y))
    tempx = x + a*math.exp(math.sin(x)+math.sin(y))*math.cos(x)
    tempy = y + a*math.exp(math.sin(x)+math.sin(y))*math.cos(y)
    if fxy != math.exp(math.sin(tempx)+math.sin(tempy)):
        x = tempx
        y = tempy
    else:
        print ('maximized output is', fxy, 'at x = ', x, 'and y = ', y)
        break
