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


class Solution(object):
    def decompressRLElist(self, nums):

        i = 0

        result = []

        while i < len(nums):

            temp_list = []
            temp_list.append(nums[i+1])

            result += nums[i] * temp_list

            i += 2

        return result
# ------------------------------------------------------------------------------------------------------------------


'''

Problem ----------------------------------------------------------------------------------------------------------


You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Runtime: 60 ms, faster than 67.79% of Python online submissions for Add Two Numbers.
'''


class Solution(object):

    def addTwoNumbers(self, l1, l2):

        total = 0
        multiplier = 1

        curr = l1
        while curr:
            total += curr.val * multiplier
            multiplier *= 10
            curr = curr.next

        curr = l2
        multiplier = 1
        while curr:
            total += curr.val * multiplier
            multiplier *= 10
            curr = curr.next

        if total == 0:
            return ListNode(0)

        l3 = ListNode(1)
        curr = l3
        while total > 0:
            curr.next = ListNode(total % 10)
            total = total // 10
            curr = curr.next
        l3 = l3.next
        return l3

# ------------------------------------------------------------------------------------------------------------------
