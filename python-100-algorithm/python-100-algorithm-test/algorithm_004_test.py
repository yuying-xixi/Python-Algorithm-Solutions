def test1():
    for cock in range(0, 21):
        for hen in range(1, (100 - 5*cock)//3 + 1):
            chicken = 100 - cock - hen
            if 5*cock + 3*hen + chicken/3 ==100 :
                print("公鸡, 母鸡, 小鸡, 价格:", cock, hen, chicken, 5*cock + 3*hen + chicken/3)

def test2():
    cock = 0
    while cock <= 20:
        hen = 0
        while hen <= 33:
            chicken = 100 - hen - cock
            if 5*cock + 3*hen + chicken/3 ==100:
                print("公鸡, 母鸡, 小鸡, 价格:", cock, hen, chicken, 5*cock + 3*hen + chicken/3)
            hen += 1
        cock +=1

def test3():
    cock = 0
    while cock <= 20:
        hen = 0
        while hen*3 <= 100 - cock*5:
            chicken = 100 - hen - cock
            if 5*cock + 3*hen + chicken/3 ==100:
                print("公鸡, 母鸡, 小鸡, 价格:", cock, hen, chicken, 5*cock + 3*hen + chicken/3)
            hen += 1
        cock +=1
