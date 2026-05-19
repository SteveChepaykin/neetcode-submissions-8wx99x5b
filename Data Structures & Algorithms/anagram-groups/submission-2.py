class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for s in strs:
            sorts = ''.join(sorted(s))
            if out.get(sorts):
                out[sorts].append(s)
            else:
                out[sorts] = [s]
        return list(out.values())