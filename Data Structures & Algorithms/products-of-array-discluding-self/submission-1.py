class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return 0
        prefs = [1]
        sufs = [1]
        for i in nums:
            prefs.append(prefs[-1] * i)
        for i in nums[::-1]:
            sufs.append(sufs[-1] * i)
        print(prefs)
        print(sufs)
        out = []
        sufs.reverse()
        for i in range(len(nums)):
            out.append(prefs[i]*sufs[i+1])
        return out