# Reverse-Integer


### Problem statement : Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

### Results:
![Results rverse integer](https://user-images.githubusercontent.com/75063039/135732052-9b3cdadc-6013-446c-bbeb-91dfdfa32718.png)

### Previous submissions  : 
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)
        negative = '-' in x_str
        mirror = int(x_str.replace("-","")[::-1])
        
        if mirror < 2**31-1:
            if negative:
                return mirror*-1
            else:
                return mirror
        else:
            return 0
'''
![Results rverse integer](https://user-images.githubusercontent.com/75063039/135732111-e23db611-7c57-4feb-afd8-6c109127744e.png)
