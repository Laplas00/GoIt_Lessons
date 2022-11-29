import turtle


class Vector:

    N = 4
    Values = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cur = 0
        self.Values.append(x)
        self.Values.append(y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"X: {self.x}\nY: {self.y}"

    def __call__(self):
        print('hello')

    def __iter__(self):
        print('iter')
        for i in range(len(self.Values)):
            yield f'{self.Values[i]}-suka'
        print('fin iter')


class Iter:
    N = 3

    def __init__(self):
        self.values = ['drug', 'sugar', 'albinos',
                       '098765', '345678', 'kofka', 'popka']
        self.cur = 0

    def __next__(self):
        if self.cur < self.N:
            self.cur += 1
            return self.values[self.cur - 1]
        else:

            raise StopIteration


class TestIter:
    def __iter__(self):
        return Iter()


test = TestIter()

for i in test:
    print(i)


# v1 = Vector(10, 20)
# v2 = Vector(40, 19)
# v3 = v1 + v2
# for i in v3:
#     print(i)
# print(v3)
