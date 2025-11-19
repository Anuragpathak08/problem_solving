class Solution:
    def twoSum(self, nums, target: int):
        hmap = {}
        out = []
        for i in range(len(nums)):
            if (target - nums[i]) in hmap:
                out.extend((hmap[target-nums[i]],i))
                break
            hmap[nums[i]]=i
        return out   