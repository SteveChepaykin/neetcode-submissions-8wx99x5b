class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        if N == 0:
            return -1
        if N == 1:
            return 0 if nums[0]==target else -1
        l, r = 0, N-1
        while l <= r:
            mid = (r+l)//2
            midd, numl, numr = nums[mid], nums[l], nums[r]
            if midd == target:
                return mid
            if numl <= midd:
                if numl <= target < midd:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if midd < target <= numr:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1