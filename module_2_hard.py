def list(x):
    result = []
    for i in range(1, (x + 1)):
        if x % i == 0:
            result.append(i)
    return (result)

def new_list(y):
    str_ = ""
    for j in range (len(y)):
        if y[j] == 1:
            continue
        for k in range (1, y[j]+1):
            chislo_1 = y[j] - k
            chislo_2 = y[j] - chislo_1
            str_ = str_ + str(chislo_1) + str(chislo_2)
    return(str_)


x = int(input("Введите число: "))
y = list(x)
z = new_list(y)
print(z)
