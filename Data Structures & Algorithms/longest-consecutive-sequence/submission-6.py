class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        curmax = 1
        nums.sort()
        prev = [nums[0]]
        for i in nums[1:]:
            if i in prev:
                continue
            else:
                if i == prev[-1]+1:
                    prev.append(i)
                else:
                    curmax = max(curmax, len(prev))
                    prev = [i]
        curmax = max(curmax, len(prev))
        return curmax
                    