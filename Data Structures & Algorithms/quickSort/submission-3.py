# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self._quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def _quickSortHelper(self, arr, start, end):
        if start >= end:
            return

        pivot = arr[end]
        left = start

        for current in range(start, end):
            if arr[current].key < pivot.key:
                arr[left], arr[current] = arr[current], arr[left]
                left += 1

        arr[left], arr[end] = arr[end], arr[left]

        self._quickSortHelper(arr, start, left - 1)
        self._quickSortHelper(arr, left + 1, end)
