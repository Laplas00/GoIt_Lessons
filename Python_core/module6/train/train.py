
# fh.seek(0)
# second = fh.read(5)
# print(second)
# fh.close()


fh = open("test.txt", "w+")
fh.write('hello, my name is bogdan')
fh.read()

position = fh.tell()
print(position)

fh.seek(1)
positionposition = fh.tell()
print(position)

fh.seek(2)
position = fh.tell()
print(position)

fh.seek(11)
fh.read()

fh.close
