import math
i = 0
x = 0
a = 0.1
for i in range(500):
    fx = math.exp(math.sin(x))
    tempx = x + a*(math.exp(math.sin(x)))*math.cos(x)
    if fx != math.exp(math.sin(tempx)):
        x = tempx
    else:
        print ('maximized value is', math.exp(math.sin(tempx)), 'at x = ', x)
        break
