
class SuperNumber:

    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return SuperNumber(str(self.value) + str(other.value))
    def __str__(self):
        return "DEBUG Value is " + str(self.value)

s_number1 = SuperNumber(1)
s_number2 = SuperNumber("Sam")

print(s_number1)

x = s_number1 + s_number2

print(x)
