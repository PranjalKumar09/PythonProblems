class Solution(object):
    def fib(self, n):
        if n < 2:
            return n
        last, second_last = 1,0
        for i in range(2,n+1):
            sum = last + second_last
            second_last = last
            last = sum
            
            
        return last
        