"""
题目描述
实现一个程序search_matrix(matrix)，参数matrix一是个仅包含 0 或 1 两种数字的矩阵，
程序应返回输入矩阵中包含的最大正方形子矩阵(长和宽相等)的区域面积。
例如:如果matrix是["1010111111","0000000111","1010110111","0000110001"]
那么它看起来像下面的矩阵：
1010111111
0000000111
1010110111
0000110001
对于上面的输入，最大的子矩阵是全部由 1 组成的一个 
3
×
3
3×3 的矩阵，
程序只需要返回最大子矩阵的面积即可，如上面的矩阵即返回 9。

输入描述
第一行输入为一个数字 
�
N，代表下面有几行
第二行到第 
�
−
1
N−1 行是代表矩阵的 0 和 1 组成的字符串，每行的长度相同

输出描述
返回一个数字，代表输入矩阵的最大正方形子距阵的面积

示例一
输入
3
110
111
110
输出
4
示例二
输入
8
1010111111
0000000111
1010110111
0000111111
1010111111
0000001111
1010111111
0000110001
输出
16
说明
可能存在多个子矩阵，返回面积最大的一个

示例三
输入
1
1001111111
输出
1
说明
可以存在单行或者单列的矩阵（
1
×
1
1×1）
"""


def search_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    # 创建一个dp矩阵

    maxSize = 0

    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = int(matrix[i][j])
            elif matrix[i][j] == "1":
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            else:
                dp[i][j] = 0
            if dp[i][j] > maxSize:
                maxSize = dp[i][j]
    print(dp)
    print(maxSize * maxSize)


if __name__ == "__main__":
    n = int(input())
    mList = [input() for _ in range(n)]
    search_matrix(mList)