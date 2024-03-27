class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)-1,1, -1):
            max_len = nums[i]
            other_two_sum = nums[i-1] + nums[i-2]
            if other_two_sum > max_len:
                return other_two_sum + max_len

        return 0