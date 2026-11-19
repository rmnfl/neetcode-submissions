# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self._merge_sort(pairs, 0, len(pairs))

        return pairs

    def _merge_sort(self, arr, s, e):
        if (e - s + 1) <= 1:
            return arr

        m = (s + e) // 2

        self._merge_sort(arr, s, m)
        self._merge_sort(arr, m + 1, e)

        self._merge(arr, s, m, e)

    def _merge(self, arr, s, m, e):
        L = arr[s : m + 1]
        R = arr[m + 1 : e + 1]

        l = r = 0
        k = s
        while l < len(L) and r < len(R):
            if L[l].key <= R[r].key:
                arr[k] = L[l]
                l += 1
            else:
                arr[k] = R[r]
                r += 1
            k += 1

        while l < len(L):
            arr[k] = L[l]
            l += 1
            k += 1

        while r < len(R):
            arr[k] = R[r]
            r += 1
            k += 1
