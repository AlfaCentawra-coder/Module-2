def result(x):
    result = []
    for i in range(1, (x + 1)):
        if x % i == 0:
            result.append(i)
    return (result)

def parol(y):
    parol = []
    for j in range(len(y)):
        if y[j] == 1:
            continue
        for k in range(1, y[j]):
            str_ = ''
            chislo_1 = y[j] - k
            chislo_2 = y[j] - chislo_1
            str_ = str(chislo_2) + str(chislo_1)
            parol.append(str_)
    return parol


x = int(input("Введите число: "))
y = result(x)
print(parol(y))
