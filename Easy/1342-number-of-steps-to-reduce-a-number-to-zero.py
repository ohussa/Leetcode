Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

"""Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it."""
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
...         #Method1:
...         #print('num at start' +str(num)+'')
...         #counter=0
...         #while num!=0:
...         #    #print('num start while' +str(num)+'')
...         #    if not(num%2):
...         #        num=num/2
...         #        #print('num after div' +str(num)+'')
...         #        counter+=1
...         #    else:
...         #        num-=1
...         #        #print('num after sub' +str(num)+'')
...         #        counter+=1
...         #return counter
...         
...         #Method2:
... 
...         #USING BITS MAY MAKE DIVISION FASTER(bitwise operations)
...         #JUST SHIFT BITS
...         #HENCE BIT IN ALGO BELOW
...         counter=0
...         #print('num at start:' +str(num)+'')
...         while num!=0:
...             #print('num at start of while:' +str(num)+'')
...             if num & 1:
...                 # bitwise mask, when do & with 1, means
...                 #last bit 1(ie odd) or not
...                 num -= 1
...                 counter+=1
...                 #print('num after subtraction by one:' +str(num)+'')
...             else:
...                 #last bit 0 (2^0) is 
...                 num >>= 1  # shifting in binary numbers
...                 #fast way of division by 2
...                 counter+=1
...                 #print('num after div:' +str(num)+'')
...         return counter
...         
...         
