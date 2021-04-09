#Exproximations

b1 = int(input("Give base 1:"))
b2 = int(input("Give base 2:"))

if b2 == b1:
    print("lol")

if b1 > b2:
    temp = b1
    b1 = b2
    b1 = temp

upp = int(input("Give the upper exponential limit:"))

c1 = 0
c2 = 0
small = 0
f1 = 1
f2 = 1
t1 = 0
t2 = 0

while c1 < upp and c2 < upp:
    if f1 > f2:
        f2 *= b2
        c2 += 1
        hold = min(f1/f2, f2/f1)
        if hold > small:
            t1 = c1
            t2 = c2
            small = hold
        print(f1, c1, f2, c2, hold)
    else:
        f1 *= b1
        c1 += 1
        hold = min(f1/f2, f2/f1)
        if hold > small:
            t1 = c1
            t2 = c2
            small = hold
        print(f1, c1, f2, c2, hold)
print("The min ratio was " + str(b1) + "^" + str(t1) + " divided by " + str(b2) + "^" + str(t2) + ": which is " + str(small))
