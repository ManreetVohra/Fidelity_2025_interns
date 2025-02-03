#How to use a decorater
def decorater(fun):
    def wrapper(a,b):
        print("Adding")
        print(fun(a,b))
        print("end")
    return wrapper

@decorater
def add(x,y):
    return (x+y)

add(10,20)