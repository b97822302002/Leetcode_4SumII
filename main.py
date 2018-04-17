class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        twosum_table = {}
        count = 0
        for a in A:
            for b in B:
                if a+b in twosum_table:
                    twosum_table[a+b] += 1
                else:
                    twosum_table[a+b] = 1
        for c in C:
            for d in D:
                if -(c+d) in twosum_table:
                    count += 1
        return count
        
