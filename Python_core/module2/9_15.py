first = 375
second = 575

print("First num -", first)
print("Second num -", second)

nod = 0

gcd = min(first, second)

# Была проблема с этой задачей, но суть заключалась в том
# что  надо по отдельности их проверять
# оператор and не способен проверять 2 деления
while True:
    if first % gcd == 0:
        if second % gcd == 0:
            print("yes it is -", gcd)
            break
        else:
            gcd -= 1
            continue
    else:
        gcd -= 1
        continue


print("finish -", gcd)


# Успешно
