"""
Given an unsorted integer array, find the smallest missing positive integer.

Input: [1,2,0]
Output: 3

Input: [3,4,-1,1]
Output: 2

Input: [7,8,9,11,12]
Output: 1

"""


def firstMissingPositive(nums):
    nums = [num for num in nums if num > 0]
    if not nums:
        return 1
    else:
        nums = sorted(nums)
        if nums[0] > 1:
            return 1
        else:
            for index in range(len(nums)-1):
                if nums[index+1] - nums[index] > 1:
                    return nums[index]+1
            return nums[-1] + 1


print(firstMissingPositive([1, 2, 3, 4, 5]))
