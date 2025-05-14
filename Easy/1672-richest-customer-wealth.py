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
        maxWealth=[]
        maxWealth.append(0)
        val=0

        for customer in accounts:
            for cus_accounts in customer:
                val+=cus_accounts
            if val>maxWealth[0]:
                maxWealth.insert(0,val)
            else:
                maxWealth.append(val)
            val=0
        return maxWealth[0]
