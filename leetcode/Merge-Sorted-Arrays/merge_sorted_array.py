class Solution(object):
    def merge(self, num1, m, num2, n):
        """
        :type num1: List[int]
        :type m: int
        :type num2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        f = []
        xi = 0
        yi = 0
        list_obj = None
        
        for _ in range(m+n): 
            if xi == m and yi < n:
                f.append(num2[yi])
                yi += 1
            elif yi == n and xi < m:
                f.append(num1[xi])
                xi += 1

            elif num1[xi] <= num2[yi]:
                f.append(num1[xi])                
                xi += 1                
            else:
                f.append(num2[yi])                
                yi += 1

            # print(f"num1  = {num1}, xi = {xi}")
            # print(f"num2  = {num2}, yi = {yi}")
            # print(f"final = {f}")
            # print('\n')
        for i, e in enumerate(f):
            num1[i] = e


num1 = [1,2,3,0,0,0]
m = 3
num2 = [2,5,6]
n = 3

solution = Solution()
solution.merge(num1, m, num2, n)
