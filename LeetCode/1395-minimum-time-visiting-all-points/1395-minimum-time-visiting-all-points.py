class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        time=0
        for i in range(len(points)-1):
            x1,y1=points[i]
            x2,y2=points[i+1]
            time_travel=max(abs(x2-x1),abs(y2-y1))
            time+=time_travel
        return time