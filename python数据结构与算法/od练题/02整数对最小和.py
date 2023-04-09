"""
题目描述
给定两个整数数组 array1 array2
数组元素按升序排列
假设从array1 array2中分别取出一个元素可构成一对元素
现在需要取出K个元素
并对取出的所有元素求和
计算和的最小值
注意：
两对元素如果对应于array1 array2中的两个下标均相同，则视为同一个元素

输入描述
输入两行数组array1 array2
每行首个数字为数组大小 size( 0 < size <= 100)
0 < array1(i) <= 1000
0 < array2(i) <= 1000
接下来一行为正整数k (0 < k <= array1.size() * array2.size())

输出描述
满足要求的最小和

示例一
输入
3 1 1 2
3 1 2 3
2
输出
4
说明
用例中，需要取两个元素 取第一个数组第0个元素 与第二个数组第0个元素，组成一对元素[1,1]
取第一个数组第1个元素 与第二个数组第0个元素，组成一对元素[1,1]
求和为1+1+1+1=4 为满足要求的最小和

"""


def func():
    array1Info = input().split()
    array2Info = input().split()
    k = int(input())
    array1Size = int(array1Info[0])
    array1 = array1Info[1:]
    array2Size = int(array2Info[0])
    array2 = array2Info[1:]
    sumList = []
    for a in array1:
        for b in array1:
            sumList.append(int(a) + int(b))
    sumList.sort()
    sums = 0
    for i in range(k):
        sums += sumList[i]
    print(sums)




if __name__ == '__main__':
    func()
