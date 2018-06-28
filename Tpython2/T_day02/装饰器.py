# coidng=utf-8
def w1(func):
    def inner():
        print("---inner---")
        if func.__name__ == "f1":
            func()
        else:
            print("没有权限")

    return inner


@w1
def f1():
    print("---f1----")


@w1
def f2():
    print("---f2----")


f1()
