"""
问题描述
有⼀对兔⼦，从出⽣后的第3个⽉起每个⽉都⽣⼀对兔⼦。
⼩兔⼦⻓到第3个⽉后每个⽉⼜⽣⼀对兔⼦，
假设所有的兔⼦都不死，
问30个⽉内每个⽉的兔⼦总对数为多少？

问题分析
月份与兔子数量分析
1个月的兔子   2个月的兔子  3个月及以上的兔子 兔子的总数  本月新生兔子
1             0            0                 1           0
0             1            0                 1           0
1             0            1                 2           1
1             1            1                 3           1
2             1            2                 5           2           
3             2            3                 8           3
2             3            5                 13          5
......

1月兔子 = 新生的兔子
2月兔子 = 上月1月兔子
3月兔子 = 上月2月兔子+原本的3月兔子
新生兔子 = 3月兔子

兔子总数 = 前1个月总数 + 前2个月的兔子总数

"""
"""
if __name__ == "__main__":
    month = 3
    last_1_total = 1
    last_2_total = 1

    while month <= 30:
        now_rabbit_total = last_1_total + last_2_total
        last_2_total = last_1_total
        last_1_total = now_rabbit_total
        print(f"{month}月兔子总数{now_rabbit_total}")
        month += 1
"""

# 同时计算下两个月的兔子总数
if __name__ == "__main__":
    month = 3
    last_1_total = 1
    last_2_total = 1

    while month <= 30:
        last_2_total = last_1_total + last_2_total
        last_1_total = last_2_total + last_1_total
        print(f"{month}月兔子总数{last_2_total}")
        print(f"{month+1}月兔子总数{last_1_total}")
        month += 2
