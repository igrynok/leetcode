class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        num = 0
        for i in range(len(self.hits) - 1, -1, -1):
            if timestamp - self.hits[i] < 300:
                num += 1
            else:
                break
        return num

    # Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
