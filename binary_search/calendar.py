class MyCalendar(object):

    def __init__(self):
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if len(self.events) == 0:
            self.events.append([start, end])
            return True
        first_index = self.binary_search(end)

        if first_index == -1:
            if self.events[-1][1] <= start:
                self.events.append([start, end])
                return True
            else:
                return False
        elif first_index > 0:
            if self.events[first_index - 1][1] <= start:
                self.events.insert(first_index, [start, end])
                return True
            else:
                return False
        elif first_index == 0:
            self.events.insert(0, [start, end])
            return True

    def binary_search(self, end):
        left, right = 0, len(self.events) - 1
        first_true_index = -1
        while left <= right:
            mid = (left + right) // 2
            if end <= self.events[mid][0]:
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return first_true_index

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
