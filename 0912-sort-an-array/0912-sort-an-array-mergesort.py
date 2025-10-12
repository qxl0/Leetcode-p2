class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(A):
            LA = len(A)
            if LA == 1: return A
            LH, RH = mergeSort(A[:LA//2]), mergeSort(A[LA//2:])
            return merge(LH, RH)
        def merge(L, R):
            ln, rn = len(L), len(R)
            S, i, j = [], 0,0
            while i<ln and j<rn:
                if L[i]<=R[j]:
                    S.append(L[i])
                    i += 1
                else:
                    S.append(R[j])
                    j += 1
            return S + (R[j:] if i==ln else L[i:])
        return mergeSort(nums)
        
                
                    