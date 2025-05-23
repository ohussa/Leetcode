Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Definition for singly-linked list.
... # class ListNode(object):
... #     def __init__(self, val=0, next=None):
... #         self.val = val
... #         self.next = next
... class Solution(object):
...     def middleNode(self, head):
...         """
...         :type head: Optional[ListNode]
...         :rtype: Optional[ListNode]
...         """
...         """
...         Method1:
...         current=head
...         counter=0
...         while current.next:
...             counter+=1
...             current=current.next
...         listlen=counter+1
...         mid=listlen//2
...         midele=mid+1
...         ind_mid_ele=midele-1
...         counter=0
...         curr=head
...         while counter!=(ind_mid_ele):
...             print(curr.val)
...             curr=curr.next
...             counter+=1
...             
...         return curr
...         #i first go till end and find number of nodes
...         #then len//2 add 1. This works for where 2 middle or one both
...         #then traverse again this time till middle node
...         #return middle node.
...         #time complexity becomes O(n+0.5n)"""
... 
...         #Method2
        #store each node in list
        #after we get the legnth of linkedlist
        #get the middle node
        current=head
        counter=0
        nodes_list=[]
        #while current is not null,on last node since when do 
        #current=current.next,so loop wont run again,since current.next was null
        while current:
            nodes_list.append(current)
            current=current.next
        mid_node=(len(nodes_list)//2)
        print(nodes_list[-1])
        return nodes_list[mid_node]
        
        #Method3 (Method 1 better than method2,no extra space needed so good space #complexity)
        #approach 2 4:40 of video



