'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''
import math
from typing import List

'''
#1. Approach 1 using O(n^2) time complexity cz of 2 nested for loops

nums = list(map(int,input("Enter values seperated by spaces").split()))
print(nums)

target = int(input("Please enter your target value"))

for i in range(0, len(nums)-1):
    for j in range(i+1, len(nums)):

        if nums[i] + nums[j] == target:
            l1 = [i,j]
            print(l1)

'''


'''
#2.  Approach 2 using O(n) time complexity cz of 2 independent for loops

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):

            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        # If no valid pair is found, return an empty list
        return []

s = Solution()
nums = list(map(int,input("Enter values seperated by spaces").split()))
print(nums)

target = int(input("Please enter your target value"))

s.twoSum(nums, target)


'''


'''
ans = [24,12,8,6]
t1 = [1,2,3,4]
t2 = []

for i in range(0, len(t1)):
    if i == 0:
        a = t1[i + 1] * t1[i + 2] * t1[i + 3]
        print(t1[i+1]*t1[i+2]*t1[i+3])
        t2.append(a)

    if i == 1:
        a = t1[i-1]*t1[i+1]*t1[i+2]
        print(t1[i-1]*t1[i+1]*t1[i+2])
        t2.append(a)

    if i == 2:
        a = t1[i-2]*t1[i-1]*t1[i+1]
        print(t1[i-2]*t1[i-1]*t1[i+1])
        t2.append(a)

    if i == 3:
        a = t1[i-3]*t1[i-2]*t1[i-1]
        print(t1[i-3]*t1[i-2]*t1[i-1])
        t2.append(a)


print(t2)

'''

nums = [1, 2, 3, 4]
p = 1
t2  = []

for i in range(0, len(nums)):
    if i == 0:
        nums[i]=1
        p *= math.prod(nums)
        print(nums , '                 ',p)
        t2.append(p)
        p = 1

    if i == 1:
        nums[i]=1
        p *= math.prod(nums)
        print(nums , '                 ',p)
        t2.append(p)
        p = 1

    if i == 2:
        nums[i]=1
        p *= math.prod(nums)
        print(nums , '                 ',p)
        t2.append(p)
        p = 1

    if i == 3:
        nums[i]=1
        p *= math.prod(nums)
        print(nums , '                 ',p)
        t2.append(p)
        p = 1

print(t2)