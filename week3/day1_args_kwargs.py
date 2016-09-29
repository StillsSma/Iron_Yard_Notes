def adder(number_2, number_1, message="No Message Passed", happy=True):
    print(message)
    return number_1 + number_2

print(adder(9, 4, message="Do MAth Sonn!", happy=False))

print(adder("Joel ","Likes programming"))

def add(*args):
    return (sum(args))

print(add(1, 2, 3))

def beginners_luck(*args, **kwargs):
    print(args)
    print(kwargs)
    return 1
print(beginners_luck("joel", 124124, [1,2,4,5], birthday="TOday", lol="name"))
