#解法一：排序。不得不吹一下哈哈哈，迄今为止，写得最快，而写内存最高的哈哈哈
#时间88， 内存92.好吧好吧，还是因为API的sorted写得好hh
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        length = len(nums)
        result = 0
        for i in range(0, length, 2):
            result += nums[i]
        return result


#解法二：hash，没看懂，但是感觉很牛逼
#时间on,空间on
public class Solution {
    public int arrayPairSum(int[] nums) {
        int[] arr = new int[20001];
        int lim = 10000;
        for (int num: nums)
            arr[num + lim]++;
        int d = 0, sum = 0;
        for (int i = -10000; i <= 10000; i++) {
            sum += (arr[i + lim] + 1 - d) / 2 * i;
            d = (2 + arr[i + lim] - d) % 2;
        }
        return sum;
    }
} 

