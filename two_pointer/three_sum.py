class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        answer = []
        dedup = set()

        for i in range(1, len(nums) - 1):
            first = 0
            last = len(nums) - 1

            while first < last:
                if i == first:
                    first += 1
                    continue
                if i == last:
                    last -= 1
                    continue
                if nums[first] + nums[last] + nums[i] == 0:
                    ans = [nums[first], nums[i], nums[last]]
                    ans.sort()
                    if not tuple(ans) in dedup:
                        answer.append(ans)
                        dedup.add(tuple(ans))
                    last -= 1
                    first += 1
                elif nums[first] + nums[last] + nums[i] > 0:
                    last -= 1
                elif nums[first] + nums[last] + nums[i] < 0:
                    first += 1

        return answer


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    print(Solution().threeSum(nums))