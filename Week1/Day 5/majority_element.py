class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        val = None

        for num in nums:
            if count == 0:
                val = num
            count += 1 if num == val else -1

        return val