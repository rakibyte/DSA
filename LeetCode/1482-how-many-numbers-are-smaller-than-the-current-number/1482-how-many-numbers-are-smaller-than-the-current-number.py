class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ret = []
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            ret.append(count)
        return ret
