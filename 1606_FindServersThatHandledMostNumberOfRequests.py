class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = list(range(k)) 
        busy = [] 
        res = [0] * k
        for i, a in enumerate(arrival):
            while busy and busy[0][0] <= a: 
                _, x = heapq.heappop(busy)
                heapq.heappush(available, i + (x-i)%k) 
            if available: 
                server = heapq.heappop(available) % k
                heapq.heappush(busy, (a+load[i],server))
                res[server] += 1
        m = max(res)
        return [i for i in range(k) if res[i] == m]
