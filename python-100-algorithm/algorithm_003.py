"""
问题描述
编写⽤⽜顿迭代法求⽅程根的函数。⽅程为ax**3+ bx**2+ cx+ d=0，系
数a、b、c、d由主函数输⼊，
求x在1附近的⼀个实根。
求出根后，由主函数输出。
⽜顿迭代法的公式：x = x0 - f(x0)/f'(x0)，设迭代到|x-x0|≤10**-5 时结束

⽜顿迭代法是取x0 之后，在这个基础上找到⽐x0 更接近的⽅程根，⼀步⼀步迭代，从⽽找到更接近⽅程根的近似根。
设r是f(x)=0的根，选取x0 作为r的初始近似值，过点(x0 ,f(x0 ))做曲
线y=f(x)的切线L，L的⽅程为y=f(x0 )+f'(x0 )(x-x0 )，
求出L与x轴交点的横坐标x1 =x0 -f(x0 )/f'(x0 )，称x1 为r的⼀次近似值；
过点(x1 ,f(x2 ))做曲线y=f(x)的切线，并求出该切线与x轴交点的横坐标x2 =x1 -f(x1 )/f'(x1)，称x2 为r的⼆次近似值；
重复以上过程，得到r的近似值xn 。
上述过程即为⽜顿迭代法的求解过程。
"""

def solution(a, b, c, d):
    x0 = 1.5 # 初值
    x = x0
    f = a*x**3 + b*x**2 + c*x + d
    fd = 3*a*x**2 + 2*b*x + c
    new_x = x - f/fd
    while abs(x - new_x)>1e-5:
        x = new_x
        f = a*x**3 + b*x**2 + c*x + d
        fd = 3*a*x**2 + 2*b*x + c
        new_x = x - f/fd
    return new_x

if __name__ == "__main__":
    # 输入方程系数
    print("输入方程系数:")
    a, b, c, d = map(float, input().split())
    print("方程参数为:",a, b, c, d)
    # 用牛顿迭代法求方程的根
    x = solution(a, b, c, d)
    # 输出所求方程的根
    print("输出结果 x = %.6f" %x)
