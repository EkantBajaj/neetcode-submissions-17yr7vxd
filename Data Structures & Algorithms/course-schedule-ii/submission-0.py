class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preq[crs].append(pre)
        output=[]
        cycle,visit= set(),set()
        def canTakeCourse(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in preq[crs]:
                if not canTakeCourse(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for crs in range(numCourses):
            if not canTakeCourse(crs):
                return []
        return output