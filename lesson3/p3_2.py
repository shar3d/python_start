num = input("Введите целое число: ")

if  not num.isdigit():
    print("Вы ввели какое-то говно!")
elif int(num) > 0:
    if int(num) > 10:
        print("Вы ввели число больше 10")
        if int(num) > 50:
            print("Вы ввели число больше 50")
    else:
        print("Вы ввели число меньше 10 и больше 0")
elif int (num) < -10:
    print("Вы ввели число меньше -10")
else:
    print("Вы ввели число меньше 0 и больше -10")