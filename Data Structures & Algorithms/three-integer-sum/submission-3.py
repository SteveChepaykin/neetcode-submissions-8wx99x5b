class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        if N == 0:
            return []
        nums.sort()
        out = []
        for i in range(N-2):
            num, left, right = -nums[i], i+1, N-1
            while left < right:
                res = nums[left] + nums[right]
                if res < num:
                    left += 1
                elif res > num:
                    right -= 1
                else:
                    n = [-num, nums[left], nums[right]]
                    left += 1
                    right -= 1
                    if n in out:
                        continue
                    else:
                        out.append(n)
        return out