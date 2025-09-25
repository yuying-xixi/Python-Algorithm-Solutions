
def test1():
    for i in range(1, 10):
        for j in range(10):
            if i != j:
                k = i * 1000 + i * 100 + j * 10 + j
                for temp in range(31, 100):
                    if temp * temp == k:
                        print(k)

def test2():
    flog = 0
    for i in range(1, 10):
        if flog:
            break
        for j in range(10):
            if flog:
                break
            if i != j:
                k = i * 1000 + i * 100 + j * 10 + j
                for temp in range(31, 100):
                    if temp * temp == k:
                        print(k)
                        flog = 1
