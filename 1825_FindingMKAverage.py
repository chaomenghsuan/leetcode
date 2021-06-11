from sortedcontainers import SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.q = collections.deque()
        self.sorted = SortedList()
        self.total, self.k_left, self.k_right = 0, 0, 0

    def addElement(self, num: int) -> None:
        self.total += num
        self.q.append(num)
        i = self.sorted.bisect_left(num)
        if i < self.k:
            self.k_left += num
            if len(self.sorted) >= self.k:
                self.k_left -= self.sorted[self.k-1]
        if i >= len(self.sorted) + 1 - self.k:
            self.k_right += num
            if len(self.sorted) >= self.k:
                self.k_right -= self.sorted[-self.k]
        self.sorted.add(num)
        if len(self.q) > self.m:
            num = self.q.popleft()
            self.total -= num
            i = self.sorted.index(num)
            if i < self.k:
                self.k_left -= num
                self.k_left += self.sorted[self.k]
            elif i >= len(self.sorted) - self.k:
                self.k_right -= num
                self.k_right += self.sorted[-self.k-1]
            self.sorted.remove(num)


    def calculateMKAverage(self) -> int:
        if len(self.sorted) < self.m:
            return -1
        return (self.total-self.k_left-self.k_right)//(self.m-self.k*2)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
