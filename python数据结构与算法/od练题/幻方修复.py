"""
【幻方修复】

幻方（Magic Square）是一个由 1~N²，共 N²个整数构成的 N*N 矩阵，满足每行、列和对角线上的数字和相等。
上回你已经帮助小明将写错一个数字的幻方进行了修复，小明在感谢之余也想进一步试试你的水平，于是他准备了有两个数字发生了位置交换的幻方。
你可以把这两个交换的数字找出来并且改正吗？

输入描述

第一行输入一个整数 N，代表带校验幻方的阶数（3 ≤ N ＜ 50）
接下来的 N 行，每行 N 个整数，空格隔开（1 ≤ 每个整数 ≤ N²）

输出描述

输出两行，代表两条纠正信息，注意先输出行号小的，若行号相同则先输出列好小的
每行输出空格隔开的三个整数，分别是：出错行号、出错列号、应填入的数字（末尾无空格）

示例1 输入输出示例仅供调试，后台判题数据一般不包含示例

输入

3
8 1 9
3 5 7
4 6 2
输出

1 3 6
3 2 9
"""

"""
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 计算每行、每列和对角线上的数字和
target_sum = sum(range(1, n*n+1)) // n

# 判断每行和每列是否等于目标和，并记录出错的位置
row_error, col_error = None, None
for i in range(n):
    row_sum, col_sum = 0, 0
    for j in range(n):
        row_sum += matrix[i][j]
        col_sum += matrix[j][i]
    if row_sum != target_sum:
        row_error = (i, target_sum - row_sum)
    if col_sum != target_sum:
        col_error = (i, target_sum - col_sum)

# 判断主对角线和副对角线是否等于目标和，并记录出错的位置
diag_sum, anti_diag_sum = 0, 0
for i in range(n):
    diag_sum += matrix[i][i]
    anti_diag_sum += matrix[i][n-i-1]
if diag_sum != target_sum:
    if not row_error or row_error[0] != col_error[0]:
        row_error = (col_error[0], target_sum - diag_sum)
    elif not col_error or col_error[1] != row_error[1]:
        col_error = (row_error[1], target_sum - diag_sum)
if anti_diag_sum != target_sum:
    if not row_error or row_error[0] != n-col_error[0]-1:
        row_error = (n-col_error[0]-1, target_sum - anti_diag_sum)
    elif not col_error or col_error[1] != n-row_error[0]-1:
        col_error = (n-row_error[0]-1, target_sum - anti_diag_sum)

# 输出纠正信息
print(row_error[0]+1, col_error[0]+1, matrix[row_error[0]][col_error[0]]+row_error[1]-col_error[1])
print(col_error[0]+1, row_error[0]+1, matrix[row_error[0]][col_error[0]]+col_error[1]-row_error[1])

"""


def func():
    n = int(input())
    magicSquareList = [list(map(int, input().split())) for i in range(n)]
    # 行
    for i in range(n*n - 1):
        for j in range(i+1, n*n):
            pass


if __name__ == "__main__":
    func()
