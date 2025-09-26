"""
问题描述
中国古代数学家张丘建在他的《算经》中提出了⼀个著名的“百钱百鸡问题”：
⼀只公鸡值五钱，⼀只⺟鸡值三钱，三只⼩鸡值⼀钱，
现在要⽤百钱买百鸡，请问公鸡、⺟鸡、⼩鸡各多少只？

问题分析
设公鸡, 母鸡, 小鸡数量分别为cock, hen, chicken,可列出式子
1. cock + hen + chicken = 100
2. 5cock + 3hen + chicken/3 = 100

其中公鸡最多可以买20只, 母鸡最多可以买33只, 小鸡最多100只
"""
"""
for cock in range(0, 21):
    for hen in range(1, (100 - 5*cock)//3 + 1):
        chicken = 100 - cock - hen
        if 5*cock + 3*hen + chicken/3 ==100 :
            print("公鸡, 母鸡, 小鸡, 价格:", cock, hen, chicken, 5*cock + 3*hen + chicken/3)
"""
cock = 0
while cock <= 20:
    hen = 0
    while hen <= 33:
        chicken = 100 - hen - cock
        if 5*cock + 3*hen + chicken/3 ==100:
            print("公鸡, 母鸡, 小鸡, 价格:", cock, hen, chicken, 5*cock + 3*hen + chicken/3)
        hen += 1
    cock +=1
