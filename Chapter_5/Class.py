# Class.py

class FourCal():

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

# ----------------------------------------------------------

a = FourCal(4, 2)
# a.setdata(4, 2)
print(a.first)
print(a.second)

print("덧셈: ", a.add())

print("뺄셈: ", a.sub())

print("곱셈: ", a.mul())

print("나눗셈: ", a.div())

# ----------------------------------------------------------

class MoreCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

    def div(self):

        if self.second == 0:
            return 0
        else:
            return self.first / self.second

# ----------------------------------------------------------

A = MoreCal(4, 3)

print(A.pow())

A = MoreCal(4, 0)

print(A.div())

# ----------------------------------------------------------

class Family:
    lastname = "김"

# ----------------------------------------------------------

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

print(id(a.lastname))
print(id(b.lastname))
