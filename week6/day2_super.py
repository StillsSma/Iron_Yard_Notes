#Example of useing Super()

class A:

    def __init__(self):
        self.ready = True

class B(A):

    def __init__(self, favorite):
        super().__init__()
        self.favorite = favorite

x = A()
print(x.ready)

y = B("Jelly Beans")

print(y.ready)
