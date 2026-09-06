class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = dict(Counter(nums))
        sorted_count=sorted(count.items(),key=lambda x:x[1],reverse=True)
        return [x[0] for x in sorted_count[:k]]



        