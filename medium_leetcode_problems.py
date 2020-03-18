'''
Problem ----------------------------------------------------------------------------------------------------------
Given an array nums containing n + 1 integers 
where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

Runtime: 52 ms, faster than 73.64% of Python online submissions for Find the Duplicate Number.

'''


def findDuplicate(nums):
    m_set = set()
    for num in nums:
        if num not in m_set:
            m_set.add(num)
        else:
            return num
# ------------------------------------------------------------------------------------------------------------------
