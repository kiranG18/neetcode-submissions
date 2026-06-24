class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Seen = {}
        for i, num in enumerate(nums):
            need = target - num

            if need in Seen:
                return[Seen[need],i]
            Seen[num] = i