# Сумирует числа по последовательности от 1


sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    else:
        for i in range(1, num + 1):
            print(f"{i} + {sum} = {sum}")
            sum += i
    print(sum, " sum")
