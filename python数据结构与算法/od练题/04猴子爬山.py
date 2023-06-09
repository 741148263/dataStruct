"""
猴子爬山
题目描述
一天一只顽猴想要从山脚爬到山顶，
途中经过一个有n个台阶的阶梯，
但是这个猴子有个习惯，每一次只跳1步或3步
试问？猴子通过这个阶梯有多少种不同的跳跃方式

输入描述
输入只有一个数n， 0 < n < 50
代表此阶梯有多个台阶

输出描述
有多少种跳跃方式

示例一
输入
50
输出
122106097
示例二
输入
3
输出
2
"""


def jump(n):
    # n = 1 或者n = 2的时候都只有一种方式，n = 3 的时候有两种，后续的所有都需要考虑两种场景，3 和 1。所以使用递归思想完成跳跃
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    return jump(n - 3) + jump(n - 1)


print(jump(50))
