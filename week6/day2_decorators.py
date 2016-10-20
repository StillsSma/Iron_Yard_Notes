# you can use functions to call other functions

def function_caller(func):
     print("Code hax")
     return func

@function_caller
def remote_control():
    print("i love lamp")
    return 0

remote_control()
