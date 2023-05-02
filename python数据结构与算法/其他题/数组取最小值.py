"""
给定一个数组，可以给数组添加一个限制使得数组中的每一个数和限制取min，要使数组的总和不超过 total，
求限制最高可以取多少，如果不需要限制则返回-1。

输入第一行包含两个整数n，m(1 ≤ n,m,ai ≤ 100000)，分别代表数组的长度和不能超过的数组的总和。

第二行包含n个整数，代表数组的每个元素。
输入：
5 12
1 2 3 4 5

输出：
3

输入：
5 15
1 2 3 4 5

输出：
-1
"""

def func():
    liLen, total = input().split()
    li = input().split()
    sum = 0
    for index, value in enumerate(li):
        sum += int(value)
        if sum > int(total):
            return index - 1
    else:
        return -1



if __name__ == "__main__":
    print(func())