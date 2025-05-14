Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution(object):
...     def runningSum(self, nums):
...         """
...         :type nums: List[int]
...         :rtype: List[int]
...         """
...         runningSums=nums
...         for i in range(1,len(runningSums)):
...             runningSums[i]=runningSums[i-1]+runningSums[i]
