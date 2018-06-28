# coding=utf-8
class Test():
    def __init__(self, func):
        print("--chushihua---")
        print("func name is %s" % func.__name__)
        self.__func = func

    def __call__(self, *args, **kwargs):
        print("call")
        self.__func()


@Test
def test():
    print("-----test----")


test()

