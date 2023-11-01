class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:

        self.requests.append(t)

        left, right = 0, len(self.requests) - 1
        first_true_index = -1
        while left <= right:
            mid = (right + left)//2
            if self.requests[mid] >= t - 3000:
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return len(self.requests) - first_true_index

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)