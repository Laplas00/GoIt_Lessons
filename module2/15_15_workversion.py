result = None
operand = None
operator = None
wait_for_number = True
sum = 0


if sum == 0:
    while True:
        try:
            sum = float(input("Начальное число: "))
            if type(sum) == int or float:
                break
            else:
                print('Это какаха а не цифра')
                continue
        except ValueError:
            print('Мне нужно число так то')
            print('Давай еще раз')
            continue
else:
    pass


while wait_for_number:
    print(sum)
    operator = input("Оператор:  ")
    if operator == "=":
        print(sum)
        break
    elif operator not in "+-=/*":
        print("Тебе нужно и пользовать + - * / или =")
        continue
    else:
        while wait_for_number:
            try:
                operand = int(input("Рабочее число: "))
                if type(operand) == int or float:
                    print("инт и флоат")

            except:
                print('Мне нужно именно число')
                print('Еще разокк')
                continue
            try:
                if operator == "+":
                    print(f"operand = {operand}, sum = {sum}")
                    sum += operand
                    print(f"operand = {operand}, sum = {sum}")
                    break
                if operator == "-":
                    print(f"operand = {operand}, sum = {sum}")
                    sum -= operand
                    print(f"operand = {operand}, sum = {sum}")
                    break
                if operator == "*":
                    print(f"operand = {operand}, sum = {sum}")
                    sum *= operand
                    print(f"operand = {operand}, sum = {sum}")
                    break
                if operator == "/":
                    print(f"operand = {operand}, sum = {sum}")
                    sum /= operand
                    print(f"operand = {operand}, sum = {sum}")
                    break
            except ZeroDivisionError:
                print('Деление на ноль дорогой, давай другое')
                continue
result = sum
