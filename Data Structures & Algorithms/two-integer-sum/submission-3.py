class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i, num in enumerate(nums):
            counterpart = target - num

            if counterpart in store:
                return [store[counterpart], i]

            store[num] = i