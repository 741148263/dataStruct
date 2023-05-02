"""
■ 题目描述

【回文字符串】

如果一个字符串正读和反渎都一样（大小写敏感），则称它为一个「回文串」，例如：

leVel是一个「回文串」，因为它的正读和反读都是leVel；同理a也是「回文串」
art不是一个「回文串」，因为它的反读tra与正读不同
Level不是一个「回文串」，因为它的反读leveL与正读不同（因大小写敏感）
给你一个仅包含大小写字母的字符串，请用这些字母构造出一个最长的回文串，若有多个最长的，返回其中字典序最小的回文串。

字符串中的每个位置的字母最多备用一次，也可以不用。

输入

abczcccddzz
输出

ccdzazdcc
示例2 输入输出示例仅供调试，后台判题数据一般不包含示例

输入

ABabBabA
输出

ABabbaBA

"""
from collections import defaultdict


def func(s):
    # 1. 先统计每一个字符出现的次数
    countDict = defaultdict(int)
    for i in s:
        countDict[i] += 1
    print(countDict)
    # countDict进行排序,并且删除单个元素
    countMuchDict = {k: v for k, v in sorted(countDict.items(), key=lambda item: ord(item[0])) if v != 1}
    countOneDict = {k: v for k, v in sorted(
        countDict.items(), key=lambda item: item[1]) if v == 1}
    print(countMuchDict)
    print(countOneDict)
    # 3. 开始拼接新的字符串
    for k, v in countMuchDict.items():
        pass

    

target = "abczcccddzz"
func(target)
