def test():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1


t = test()
print(next(t))
print(t.send("HAHAHAH"))