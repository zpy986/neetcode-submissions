class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carlist = [(position[i], speed[i]) for i in range(len(position))]
        carlist.sort(key = lambda x:-x[0])

        stack = []

        for pos, speed in carlist:
            time = (target - pos) / speed
            if not stack:
                stack.append(time)
            else:
                last_time = stack[-1]
                if time > last_time:
                    stack.append(time)
        
        return len(stack)

