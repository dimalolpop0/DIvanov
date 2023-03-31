 x=float(input("Напишите Первое Число"))
 y=float(input("Напишите Второе Число"))
 z=float(input("Вот Наша Сумма "))
 if x+y==z:
     print("Юхуу, Урааа")
 elif x+y!=z:
     print("Фууу, Неверно")
     print(x+y)
     
num, num2 = int(input("Введите пробег (трехзначное число) = ")), int(input("Введите число ="))
if num in range(100,999) and num2 in range(24,79):
    x = num // 100
    y = (num % 100) // 14
    z = num % 14
    num = x + y + z
    if num > num2:
        num = 0 
        print("Сброс,", "пробег = ", num)
    else:
        print("Сегодня работает,", "пробег = ", num)
else:
    print("Второе число должно двухзначным")