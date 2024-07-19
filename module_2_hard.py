def dividers(x):
    d = []
    for i in range(2, x + 1 ):
        if x % i == 0:
            d.append(i)
    return d

def password(divs):
    psswrd = []
    for i in range(1, max(divs)):
        for d in divs:
            if (i < d):
                if not(str(d - i) + str(i) in psswrd):
                    psswrd.append(str(i) + str(d - i))
    return psswrd


x = int(input("Введите число: "))
d = dividers(x)
p = password(d)
for i in range(len(p)):
    print(p[i], end="")
