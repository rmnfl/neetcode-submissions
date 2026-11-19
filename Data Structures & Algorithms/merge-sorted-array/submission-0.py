class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        L = nums1[0 : m]
        R = nums2[0 : n]

        l = r = k = 0

        while l < len(L) and r < len(R):
            if L[l] <= R[r]:
                nums1[k] = L[l]
                l += 1
            else:
                nums1[k] = R[r]
                r += 1
            k += 1

        while l < len(L):
            nums1[k] = L[l]
            l += 1
            k += 1
        
        while r < len(R):
            nums1[k] = R[r]
            r += 1
            k += 1