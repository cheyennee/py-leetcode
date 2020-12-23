#解法一：排序+指针，时间96，内存30
class Solution(object):
    def intersect(self, nums1, nums2):
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        result = []
        head1, head2 = 0, 0
        length1, length2 = len(nums1), len(nums2)
        while head1< length1 and head2 < length2:
            if (nums1[head1] == nums2[head2]):
                result.append(nums1[head1])
                head1 += 1
                head2 += 1
            elif nums1[head1] < nums2[head2]:
                head1 += 1
            else:
                head2 += 1
        return result

