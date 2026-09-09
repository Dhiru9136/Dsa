# 1480. Running Sum of 1d Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
 

class Solution(object):
    def runningSum(self, nums):
        result=[0]
        for i in nums:
            last_element=result[-1]+i
            result.append(last_element)
        result.pop(0)
        return result


obj=Solution()
print(obj.runningSum([555,901,482,1771]))

