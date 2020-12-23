#解法一：排序+遍历，时间92，内存68，但是我感觉好像不应该这么复杂
#好的，看了官方题解，这真的是最快的解法
class Solution(object):
    def intersection(self, nums1, nums2):
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        result = []
        head1, head2 = 0, 0
        length1, length2 = len(nums1), len(nums2)
        while head1< length1 and head2 < length2:
            if (nums1[head1] == nums2[head2]) and nums1[head1] not in result:
                result.append(nums1[head1])
                head1 += 1
                head2 += 1
            elif nums1[head1] < nums2[head2]:
                head1 += 1
            else:
                head2 += 1
        return result


#解法二：hash表
class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return self.set_intersection(set1, set2)

    def set_intersection(self, set1, set2):
        if len(set1) > len(set2):
            return self.set_intersection(set2, set1)
        return [x for x in set1 if x in set2]

#解法三：API
class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

