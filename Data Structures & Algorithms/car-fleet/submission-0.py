class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        for p, s in pairs:
            time = (target - p) / s
            print(times, time)
            if len(times) > 0 and time <= times[-1]:
                continue
            times.append(time)
        
        return len(times)