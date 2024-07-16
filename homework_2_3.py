my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = len(my_list)
while x >= 0:
    if int(my_list[x]) > 0:
        print(my_list[x])
        x -= 1
    elif int(my_list[x]) == 0:
        continue
    else:
        break
