my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = 0
for x in range (len(my_list)):
    if int(my_list[x]) > 0:
        print(my_list[x])
        x += 1
    elif int(my_list[x]) == 0:
        continue
    else:
        break
