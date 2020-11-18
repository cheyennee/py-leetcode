#解法一：社会性死亡-^-,使用二分法优化后的暴力，时间5，内存5
class Solution(object):
    def twoSum(self, numbers, target):
        result = []
        length = len(numbers)
        for i in range(length-1):
            numj = target - numbers[i]
            left = i+1
            right = length-1
            while left<=right:
                mid = (left+right)//2
                if numbers[mid] == numj:
                    result.append(i+1)
                    result.append(mid+1)
                    return result
                elif numbers[mid] < numj:
                    left = mid+1
                else:
                    right = mid-1
        return result


#解法二：双指针，抄的,没想出来。这种解法真是太妙了，线性时间。时间56，内存19
#当左右位置的值加起来小于target时，left++;当大于target时，right--
class Solution(object):
    def twoSum(self, numbers, target):
        length = len(numbers)
        left, right = 0, length-1
        while left<right:
            temp = numbers[left]+numbers[right]
            if temp == target:
                return [left+1, right+1]
            elif temp < target:
                left += 1
            else:
                right -= 1
        return []

