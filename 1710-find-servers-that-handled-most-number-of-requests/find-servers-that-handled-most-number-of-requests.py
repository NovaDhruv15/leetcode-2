import heapq
from typing import List
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free_servers = list(range(k))   
        working = []                    
        handled = [0] * k
        for i in range(len(arrival)):
            start = arrival[i]
            time_needed = load[i]
            while working and working[0][0] <= start:
                finish_time, server = heapq.heappop(working)
                position = i + (server - i) % k
                heapq.heappush(free_servers, position)
            while free_servers and free_servers[0] < i:
                old = heapq.heappop(free_servers)
                heapq.heappush(free_servers, old + k)
            if free_servers:
                server = heapq.heappop(free_servers) % k
                heapq.heappush(working, (start + time_needed, server))
                handled[server] += 1
        most = max(handled)
        return [s for s in range(k) if handled[s] == most]