class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        output = []
        a = 0
        b = 0
        c = 0
        while a < m and b < n:
            if nums1[a] <= nums2[b]:
                element = nums1[a]
                a += 1
            else:
                element = nums2[b]
                b += 1
            output.append(element)
            c += 1
        if a == m:
            while c < m + n:
                element = nums2[b]
                output.append(element)
                b += 1
                c += 1
        else:
            while c < m + n:
                element = nums1[a]
                output.append(element)
                a += 1
                c += 1
        for i in range(0, m + n):
            nums1[i] = output[i]
