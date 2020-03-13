'''
Given the array nums, for each nums[i] find out how many numbers in the array 
are smaller than it. That is, for each nums[i] you have to count the number 
of valid j's such that j != i and nums[j] < nums[i]. Return the answer in an array.

Runtime: 40 ms, faster than 88.13% of Python online submissions for How Many Numbers 
Are Smaller Than the Current Number.

'''


def smallerNumbersThanCurrent(nums):

    sorted_nums = list(sorted(nums))
    return [sorted_nums.index(num) for num in nums]
