class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preq[crs].append(pre)
        
        visit = set()

        def canTakeCourse(crs):
            if crs in visit:
                return False
            if preq[crs]==[]:
                return True
            visit.add(crs)
            for each in preq[crs]:
                if not canTakeCourse(each):
                    return False
            visit.remove(crs)
            preq[crs]=[]
            return True
        
        for crs in range(numCourses):
            if not canTakeCourse(crs):
                return False
        
        return True