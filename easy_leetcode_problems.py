'''
Problem ----------------------------------------------------------------------------------------------------------

Given the array nums, for each nums[i] find out how many numbers in the array 
are smaller than it. That is, for each nums[i] you have to count the number 
of valid j's such that j != i and nums[j] < nums[i]. Return the answer in an array.

Runtime: 40 ms, faster than 88.13% of Python online submissions for How Many Numbers 
Are Smaller Than the Current Number.

'''


def smallerNumbersThanCurrent(nums):

    sorted_nums = list(sorted(nums))
    return [sorted_nums.index(num) for num in nums]

# ------------------------------------------------------------------------------------------------------------------


'''
Problem ----------------------------------------------------------------------------------------------------------

You're given strings J representing the types of stones that are jewels, 
and S representing the stones you have.  Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".


Runtime: 12 ms, faster than 95.33% of Python online submissions for Jewels and Stones.
'''


def numJewelsInStones(J, S):
    return sum([S.count(char) for char in J])

# ------------------------------------------------------------------------------------------------------------------
