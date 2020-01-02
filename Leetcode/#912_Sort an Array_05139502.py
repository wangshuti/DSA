class Solution:
    def sortArray(self, nums: List[int]):
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left = Solution().sortArray(nums[:mid])
        right = Solution().sortArray(nums[mid:])
        return Solution().merge(left,right)
    
    def merge(self, left, right):
        res = []
        while left and right:
            if left[0] < right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        res = res + left + right
        return res
        
