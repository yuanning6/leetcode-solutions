class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = l + ((r - l) // 2) # A
            j = half - (i + 1) - 1 # B, index_j = number - (index_i + 1) - 1

            # out of bound
            # -infinity | 0, 1, 2, 3 .... | infinity
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return ((max(Aleft, Bleft) + min(Aright, Bright)) / 2)
            else:
                # too many in left portion
                if Aleft > Bright:
                    r = i - 1
                else:
                    l = i + 1


