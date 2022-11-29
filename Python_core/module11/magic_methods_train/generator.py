def generator(n):
    for x in range(n):
        yield x*x


value = generator(20)

print(value)


a = 20
index = 0

for i in value:
    if i < a:
        print(f'{index}. {i}')
        index += 1
    else:
        break


print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
