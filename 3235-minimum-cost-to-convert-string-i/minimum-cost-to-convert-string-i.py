from collections import defaultdict
import heapq
from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int: 
        adj_list = defaultdict(list)
        for src, tgt, cst in zip(original, changed, cost):
            adj_list[src].append((tgt, cst))

        def dijkstra(src):
            pq = [(0, src)]
            min_cost_map = {src: 0}

            while pq:
                current_cost, node = heapq.heappop(pq)
                
                for nei, nei_cost in adj_list[node]:
                    new_cost = current_cost + nei_cost
                    if nei not in min_cost_map or new_cost < min_cost_map[nei]:
                        min_cost_map[nei] = new_cost
                        heapq.heappush(pq, (new_cost, nei))

            return min_cost_map
        
        unique_chars = set(source)
        min_cost_maps = {c: dijkstra(c) for c in unique_chars}
        res = 0

        for src, dst in zip(source, target):
            if src not in min_cost_maps or dst not in min_cost_maps[src]:
                return -1 
            res += min_cost_maps[src][dst]

        return res

