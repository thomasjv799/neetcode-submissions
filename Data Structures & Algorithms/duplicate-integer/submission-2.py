class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for i in nums:
            if i in hash_map:
                hash_map[i] = hash_map[i]+1
            else:
                hash_map[i] = 1

        return any(map(lambda x:x >1 ,list(hash_map.values())))

       