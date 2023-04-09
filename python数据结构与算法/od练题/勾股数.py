"""
题目描述
如果三个正整数A、B、C ，A² + B² = C² 则为勾股数，
如果ABC之间两两互质，即A与B，A与C，B与C均互质没有公约数，则称其为勾股数元组。
请求出给定 n ~ m 范围内所有的勾股数元组。

输入描述
起始范围
1 < n < 10000
n < m < 10000

输出描述
ABC保证A < B < C
输出格式A B C
多组勾股数元组，按照A B C升序的排序方式输出。
若给定范围内，找不到勾股数元组时，输出Na。

示例一
输入
1
20
输出
3 4 5
5 12 13
8 15 17
示例二
输入
5
10
输出
Na
"""
import math


def is_primary_number(number):
    """
    判断一个数是不是质数
    """
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    else:
        return True


def func1():
    """
    方法1
    """
    n = int(input())
    m = int(input())
    count = 0
    for a in range(n, m + 1):
        for b in range(a, m + 1):
            for c in range(b, m + 1):
                if a ** 2 + b ** 2 == c ** 2:
                    if any([is_primary_number(a), is_primary_number(b), is_primary_number(c)]):
                        count += 1
                        print(a, b, c)
    if count == 0:
        print("Na")


if __name__ == '__main__':
    func1()
