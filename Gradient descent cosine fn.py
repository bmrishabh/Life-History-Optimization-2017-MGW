import math
i = 0
x = 0.1
for i in range(500):
    fx = math.cos(x)
    a = 0.1
    tempx = x + (a*(math.sin(x)))
    if fx != math.cos(tempx):
        x = tempx
    else:
        print ('Minimized value is', math.cos(tempx), 'at x = ', tempx)
        break
