class test:
    t = 4
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def add(self, x:int = 1):
        self.count += x

    def __str__(self):
        return f'Name: {self.name}, count: {self.count} t: {self.t}'



t = test('t1', 5)
t.add()
t2 = test('t2', 1)
t2.add(10)
print(t)
print(t2)
test.t = 11
t3 = test('t3', 0)
print(t3)
print(t2)
print(t)
