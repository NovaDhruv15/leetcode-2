class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even, odd = 1, 0
        prefix = 0
        ans = 0
        for x in arr:
            prefix ^= (x & 1)       
            if prefix == 0:
                ans += odd          
                even += 1
            else:
                ans += even     
                odd += 1
        return ans % MOD