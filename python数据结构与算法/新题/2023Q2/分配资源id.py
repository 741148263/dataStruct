"""
■ 题目描述

【分配资源ID】

给定一个管理ID的资源池，可以从资源池中分配资源ID和释放资源ID，

分配方式有动态分配和指定分配：

动态分配是从资源池的开始分配一个资源ID
指定分配是指定一个资源ID进行分配
无论哪种分配方式释放资源ID时都需要放到资源池的尾部。

执行一系列操作后，请问资源池的第一个空闲资源ID应该是多少?

注意：

资源池的初始顺序是从小到大
资源池中空闲资源ID不足时，动态分配失败，对资源池不进行任何操作
指定分配资源ID已经被占用或者不在资源池范围内时，对资源池不进行任何操作
释放资源ID不在资源池范围内时或者已经是空闲资源ID时，对资源池不进行任何操作
保证每个用例最后都有空闲资源ID


输入描述

第一行是资源池的范围

第二行是操作个数

第三行开始，第一个数字代表操作类型，1表示动态分配，2表示指定分配，3表示释放

如果第一个数字是1，第二个表示分配的个数
如果第一个数字是2，第二个表示分配的资源ID
如果第一个数字是3，第二个表示释放的资源ID

输出描述

资源池的第一个空闲资源ID

示例1 输入输出示例仅供调试，后台判题数据一般不包含示例

输入

1 3
2
1 1
3 1
输出

2
样例说明

第一行资源池范围是[1，3]，资源池的初始顺序是1->2->3。
第二行操作个数有2个。
第三行动态分配1个资源ID，资源池中剩余的资源ID顺序是2->3。
第四行释放1个资源ID，资源ID是1，资源池中剩余的资源ID顺序是2->3->1。
执行以上操作后，资源池的第一个空闲资源ID是2。
"""


class Pool:
    def __init__(self) -> None:
        self.poolDict = {}
        self.size = 0

    def add(self, key):
        if key not in self.poolDict.keys():
            self.poolDict[key] = None
            self.size += 1

    def delete(self, key):
        if key in self.poolDict.keys():
            del self.poolDict[key]
            self.size -= 1

    def firstKey(self):
        for k in self.poolDict.keys():
            return k

def getResult(s, e, opList):
    pool = Pool()
    for i in range(start, end + 1):
        pool.add(i)

    for type, value in opList:
        if type == 1:
            while pool.size > 0 and value > 0:
                pool.delete(pool.firstKey())
                value -= 1
        elif type == 2:
            pool.delete(value)
        elif type == 3:
            if start <= value <= end:
                pool.add(value)
    print(pool.firstKey())
    


if __name__ == "__main__":
    start, end = map(int, input().split())
    opNum = int(input())
    opTV = [list(map(int, input().split())) for _ in range(opNum)]
    getResult(start, end, opTV)