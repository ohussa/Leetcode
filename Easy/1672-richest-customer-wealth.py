class Solution(object):
"""You are given an m x n integer grid accounts where accounts[i][j] is the
amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that
the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth."""
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_list=[sum(num) for num in accounts]
        return max(max_list)

#Now using list comprehension.
