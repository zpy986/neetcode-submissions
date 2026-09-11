class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.sqrt((points[i][0])**2 + (points[i][1])**2),i) for i in range(len(points))]
        heapq.heapify(distances)
        res = []
        while k:
            dis, index = heapq.heappop(distances)
            res.append(points[index])
            k-=1
        return res