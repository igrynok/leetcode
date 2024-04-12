class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

        ratios = [(w/q, q) for w, q in zip(wage, quality)]
        ratios.sort()

        paid_group = [-q for r, q in ratios[:k]]
        heapq.heapify(paid_group)
        sum_q = -sum(paid_group)

        cost = sum_q * ratios[k - 1][0]

        for ratio, quality in ratios[k:]:
            sum_q += quality + heapq.heappushpop(paid_group, -quality)
            cost = min(cost, ratio * sum_q)

        return cost