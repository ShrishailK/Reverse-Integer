class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(abs(x))
        mirror = int(x_str[::-1])
        
        if mir < 2**31-1:
            if x<=0:
                return mir*-1
            else:
                return mir
        else:
            return 0