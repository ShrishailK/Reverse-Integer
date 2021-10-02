class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(abs(x))
        mirror = int(x_str[::-1])
        
        if mirror < 2**31-1:
            if x<=0:
                return mirror*-1
            else:
                return mirror
        else:
            return 0