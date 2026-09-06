class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for i in nums:
            if i in hash_map:
                hash_map[i] = hash_map[i]+1
                return True
            else:
                hash_map[i] = 1
        return False
        

        # for i in list()
        # if len(set(hash_map.values())) > 1:
        #     return True
        # else:
        #     return False