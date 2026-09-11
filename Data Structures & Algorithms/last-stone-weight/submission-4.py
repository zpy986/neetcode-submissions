class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = - heapq.heappop(heap)
            y= - heapq.heappop(heap)

            if x == y:
                continue

            if x < y or y < x:
                new_stone = (x-y)
            
            heapq.heappush(heap, -new_stone)
        
        return -heap[0] if heap else 0
        
