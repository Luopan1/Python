from time import ctime, sleep


def timefun_arg(pre="hello"):
    def timefun(func):
        def wrappedfunc():
            print("%s	called	at	%s	%s" % (func.__name__, ctime(), pre))
            return func()

        return wrappedfunc

    return timefun


@timefun_arg("itcast")
def foo():
    print("I	am	foo")
    return "222222222"


@timefun_arg("python")
def too():
    print("I	am	too")


foo()

