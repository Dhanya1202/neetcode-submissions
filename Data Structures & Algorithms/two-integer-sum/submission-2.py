class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          store={}
          for i in range(len(nums)):
               
               counterpart=target-nums[i]
               if(counterpart in store):
                    if(store[counterpart]!=i):
                         return[store[counterpart], i]
               store[nums[i]] = i
               
          

        