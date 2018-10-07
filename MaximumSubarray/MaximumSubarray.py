# Given an integer array nums, find the contiguous subarray(containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = float('-inf')
        now_sum = 0

        for num in nums:
            if now_sum < 0:
                now_sum = max(now_sum,num)
            else:
                now_sum += num
            max_sum = max(max_sum,now_sum)

        return max_sum
    
    def test(self,nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

if __name__ == '__main__':
    sol = Solution()
    # prices = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # prices = [4, -1, 2, 1, 5]
    prices = [-1]
    print(sol.maxSubArray(prices))
