"""
■ 题目描述

【种树】

小明在直线的公路上种树，现在给定可以种树的坑位的数量和位置，以及需要种多少棵树苗，问树苗之间的最小间距是多少时，可以保证种的最均匀（两棵树苗之间的最小间距最大）？

输入描述

输入三行：

第一行：坑位的数量

第二行：坑位的位置

第三行：需要种植树苗的数量

输出描述

树苗之间的最小间距

示例1 输入输出示例仅供调试，后台判题数据一般不包含示例

输入

7
1 3 6 7 8 11 13
3
输出

6
说明

3棵树苗分别种植在1，7，13位置的坑位时，树苗种植的最均匀，最小间距为6。

"""

class Solution:
    def getMaxSpace(self):
        count = int(input())
        positionList = list(map(int, input().split()))
        treeCount = int(input())

        positionList.sort()

        low = 1
        high = positionList[-1] - positionList[0]
        ans = 0

        while low <= high:
            # 求整除
            mid = (low + high) >> 1
            if self.check(mid, positionList, treeCount):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        print(ans)

    def check(self, center, posList, treeCount):
        count = 1
        curPos = posList[0]
        for i in range(len(posList)):
            if posList[i] - curPos >= center:
                count += 1
                curPos = posList[i]
        return count >= treeCount

s = Solution()
s.getMaxSpace()