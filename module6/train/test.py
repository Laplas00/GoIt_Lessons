from pathlib import Path
import os

os.system('cd ..')

print(Path())
print(os.system('ls'))


# fh = open('test.txt', 'w')

# symbols_written = fh.write('hello')

# print(symbols_written)

# fh.close

# fh = open('test.txt', "w+")
# fh.write('Hello world!')
# fh.seek(0)

# print(fh.read(), "full")
# fh.seek(0)

# fifth_symbol = fh.read(5)

# print(fifth_symbol, '- fifth symbol')

# fh.close


fh = open('test.txt', 'w+')
fh.write("Hello\nWorld\nMy name is\nLaplas")
fh.close
fh.seek(0)


fh.seek(0)
print('----')
while True:
    print(fh.tell())
    symbol = fh.readline()
    if len(symbol) == 0:
        break
    print(symbol)
fh.seek(0)

lines = fh.readlines()
print(lines)
fh.close

print('--------------')

with open('passwd.txt', 'r') as passwd:
    print(passwd.read())
