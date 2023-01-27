
class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:

        self.requests.append(t)
        range = t - 3000
        recent_requests = 0
        n = len(self.requests)

        for i in range(n):
            if self.request[i] >= range and self.request[i] <= t:
                recent_requests += 1
            else:
                break
        
        return recent_requests