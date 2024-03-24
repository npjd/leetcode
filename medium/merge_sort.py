class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:


        def merge_sort(arr):
            n = len(arr)
            # if array length is less than one, its basically sorted....
            if n > 1:
                mid = n // 2
                left = arr[:mid]
                right = arr[mid:]

                # sort both halves
                merge_sort(left)
                merge_sort(right)

                # by the time we get here, left and right are sorted

                # do the merge
                i = j = k = 0

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1
                
                # add the remainder, only one of these loops runs
                while i < len(left):
                    arr[k] = left[i]
                    k += 1
                    i += 1
                while j < len(right):
                    arr[k] = right[j]
                    k += 1
                    j += 1

                
                
        merge_sort(nums)
        return nums