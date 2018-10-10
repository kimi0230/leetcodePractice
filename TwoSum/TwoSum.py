# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i+1,len(nums)):
                sum = nums[i] + nums[j]
                if(sum == target):
                    return [i,j]

    def twoSum2(self, nums, target):
        for i in range(0, len(nums)):

            # 想要的值減去現在的值，然後找之後的array是否有該數字
            if (target - nums[i]) in nums[i+1:]:
                return [i, nums.index(target - nums[i], i+1, len(nums))]

if __name__ == '__main__':
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target))
