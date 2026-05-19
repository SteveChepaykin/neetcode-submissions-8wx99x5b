class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        buckets = [[] for _ in range(N+1)]
        visited = []
        for i in nums:
            if i in visited:
                continue
            else:
                kolvo = nums.count(i)
                buckets[kolvo].append(i)
                visited.append(i)
        sortd = [e for l in buckets for e in l]
        return sortd[-k:]
