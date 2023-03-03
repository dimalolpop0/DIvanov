num = input("Введите  число: ")
sum = 0
for digit in num:
    sum = int(digit) + sum
print("Сумма цифр:" + str(sum))
if sum > 9:
    if sum < 100:
        print("Двузначная")
    else:
        print("Многозначная")
else:
    print("Однозначная")
