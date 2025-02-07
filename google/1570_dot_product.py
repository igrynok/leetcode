from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = {index:num for index, num in enumerate(nums) if num}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        v1 = self.vector
        v2 = vec.vector

        return sum([v1[key]*v2[key] for key in v1.keys() if key in v2.keys()])


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)