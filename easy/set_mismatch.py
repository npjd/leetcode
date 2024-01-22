class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup_num = 0
        error_set = set()
        for num in nums:
            if num in error_set:
                dup_num = num
            else:
                error_set.add(num)
        nums_set = set()
        for i in range(1,len(nums)+1):
            nums_set.add(i)
        missing_val, = nums_set.difference(error_set)
        return [dup_num, missing_val ]