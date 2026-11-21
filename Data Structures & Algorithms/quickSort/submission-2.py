# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self._quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def _quickSortHelper(self, arr, s, e):
        if e - s <= 0:
            return

        pivot = arr[e]

        l = s
        for r in range(s, e):
            if arr[r].key < pivot.key:
                arr[r], arr[l] = arr[l], arr[r] 
                l += 1

        arr[e], arr[l] = arr[l], arr[e]

        self._quickSortHelper(arr, s, l - 1)
        self._quickSortHelper(arr, l + 1, e)