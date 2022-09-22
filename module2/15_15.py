result = None
operand = None
operator = None
wait_for_number = True
sum = 0


while True:
    if operator == "=":
        print('rersult')
        print(sum)
        break
    else:
        pass
        # cilcle for num
    while wait_for_number:
        try:
            operand = int(input('>>> '))
            if operand == int:
                print(f'{operand} - is int')
                pass
            else:
                print(f'sum of all = {sum}')

        except ValueError:
            print(f'{operand} is not a num, try more')
            continue
        else:
            # cicle for operator
            while wait_for_number:
                print('--------')
                operator = input('>> ')
                if operator == '+':
                    sum += operand
                    print(sum)
                    break
                elif operator == '-':
                    sum -= operand
                    print(sum)
                    break
                elif operator == '*':
                    sum *= operand
                    print(sum)
                    break
                elif operator == '/':
                    sum /= operand
                    print(sum)
                    break
                elif operator == '=':
                    wait_for_number = False
                    print('w8tnum False')
                    print(sum)
                    break
                else:
                    print(f"{operand} is not '+' or '-' or '/' or '*'.")
                    continue
