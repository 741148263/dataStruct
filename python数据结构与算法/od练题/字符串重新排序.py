"""
题目描述：

给定一个字符串s，s包括以空格分隔的若干个单词，请对s进行如下处理后输出：

1、单词内部调整：对每个单词字母重新按字典序排序

2、单词间顺序调整：

1）统计每个单词出现的次数，并按次数降序排列

2）次数相同，按单词长度升序排列

3）次数和单词长度均相同，按字典升序排列

请输出处理后的字符串，每个单词以一个空格分隔。

输入描述：

一行字符串，每个字符取值范围：【a-zA-z0-9】以及空格，字符串长度范围：【1，1000】

示例1：

输入

This is an apple

输出

an is This aelpp

示例2：

输入：

My sister is in the house not in the yard

输出：

in in eht eht My is not adry ehosu eirsst

"""


def func(s):
    """
    这是我的思路
    """
    sList = s.split()
    for i in range(len(sList)):
        temp = [j for j in sList[i]]
        sList[i] = "".join(sorted(temp))
    countDict = {}
    for i in sList:
        count = sList.count(i)
        if not count in countDict.keys():
            countDict[count] = [i]
        else:
            temp = countDict[count]
            if not i in temp:
                temp.append(i)
                countDict[count] = temp
    countDict = {k:v for k, v in sorted(countDict.items(), key=lambda item: item[0],reverse=True)}
    exportData = []
    for key, value in countDict.items():
        # 次数相同，需要按照单词长度进行升序排列
        # 次数和单词长度均相同，按照字典升序排列
        # 策略：需要统计该次数分段中单词的长度
        # 1. 次数相同，根据长度进行升序排列
        temnewTempList = sorted(value, key=lambda item: len(item))
        # 2. 根据长度进行分割后遍历
        lenDict = {}
        for j in temnewTempList:
            jLen = len(j)
            if not jLen in lenDict.keys():
                lenDict[jLen] = [j]
            else:
                temp = lenDict[jLen]
                temp.append(j)
                lenDict[jLen] = temp
        # 3. 对该字典进行升序排列
        lenDict = {k:v for k, v in sorted(lenDict.items(), key=lambda item: item[0])}
        # 4. 对根据长度排序过的字典进行遍历，并将其写入extandData列表中
        for _, valueList in lenDict.items():
            valueList = sorted(valueList)
            for m in valueList:
                exportData.extend([m for _ in range(key)])
    print(" ".join(exportData))


from typing import List
from collections import defaultdict

def func2(arr: List[str]):
    """
    这是别人的思路
    """
    # 对所有的字符串都进行内部排序
    for i in range(len(arr)):
        arr[i] = "".join(sorted(arr[i]))
    # 统计该字符串出现的次数
    count = defaultdict(int)
    for i in arr:
        count[i] += 1
    
    arr.sort(key=lambda x: (-count[x], len(x), [ord(char) for char in x]))
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    target1 = "This is an apple"
    # in in eht eht My is not adry ehosu eirsst
    func(target1)
    func2(target1.split())
