Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Given an integer n, return a string array answer (1-indexed) where:
... 
... answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
... answer[i] == "Fizz" if i is divisible by 3.
... answer[i] == "Buzz" if i is divisible by 5.
... answer[i] == i (as a string) if none of the above conditions are true."""
... class Solution(object):
...     def fizzBuzz(self, n):
...         """
...         :type n: int
...         :rtype: List[str]
...         """
...         answer=[]
...         for i in range(1,n+1):
...             if not(i%3) and not(i%5):
...                 answer.append("FizzBuzz")
...             elif not(i%3):
...                 answer.append("Fizz")
...             elif not(i%5):
...                 answer.append("Buzz")
...             else:
...                 answer.append(str(i))
...         return answer
