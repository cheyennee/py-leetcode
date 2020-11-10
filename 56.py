'''
解法一：采用排序+合并，用时：98，内存8
时间复杂度为logn,空间复杂度为logn，主要用于排序
我抄的答案-^-

学习的知识点：1.将lambda函数用于排序 2.区间合并 3.可以合并的区间一定是连续的
'''

class Solution(object):
    def merge(self, intervals):
        #对第一个关键字进行排序
        intervals.sort(key = lambda x : x[0])
        #保存结果
        merged = []
        for interval in intervals:
            #如果结果集为空，或者现在这个区间的左值大于保存区间的最大值，则证明两者无交集，可直接将现在的区间加入结果集中
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            #否则计算两者交集
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

