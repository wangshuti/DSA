class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        l=len(nums)
        if l%2==1:
            m=(l//2)
            return nums[m]
        else:
            m=l//2
            a=nums[m]
            b=nums[m-1]
            return (a+b)/2
