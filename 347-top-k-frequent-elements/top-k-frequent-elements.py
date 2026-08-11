from typing import List
import heapq
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}

        for i in nums:
            map[i]=map.get(i,0)+1

      
        heap=[]
       
        for c,f in map.items():
            heapq.heappush(heap,(f,c))
            print(len(heap))
            if len(heap) > k:
                heapq.heappop(heap)
        return [v for c,v in heap]
