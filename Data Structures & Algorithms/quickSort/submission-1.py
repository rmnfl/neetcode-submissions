# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self._quickSort(pairs, 0, len(pairs) - 1)
        return pairs
        
    def _quickSort(self, arr, s, e):
        if e - s + 1 <= 1:
            return

        pivot = arr[e]

        i = s
        for j in range(s, e):
            if arr[j].key < pivot.key:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[e] = arr[e], arr[i]
            
        self._quickSort(arr, s, i - 1)
        self._quickSort(arr, i + 1, e)
            

        