class DynamicArray:
    
    def __init__(self, capacity: int):
        self._array = [0] * capacity
        self._curr_len = 0
        self._max_len = capacity


    def get(self, i: int) -> int:
        return self._array[i]


    def set(self, i: int, n: int) -> None:
        self._array[i] = n


    def pushback(self, n: int) -> None:
        if self._curr_len == self._max_len:
            self.resize()
        self._array[self._curr_len] = n
        self._curr_len += 1

    def popback(self) -> int:
        result = self._array[self._curr_len - 1]
        self._curr_len -= 1
        return result

    def resize(self) -> None:
        new_array = [0] * (self._max_len * 2)
        for i in range(self._curr_len):
            new_array[i] = self._array[i]

        self._array = new_array
        self._max_len *= 2

    def getSize(self) -> int:
        return self._curr_len 
        
    
    def getCapacity(self) -> int:
        return self._max_len