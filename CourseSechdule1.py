from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        preMap = { i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        visisted = set()
        def dfs(crs):
            if crs in visisted:
                return False
            if preMap[crs] == []:
                return True
            visisted.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visisted.remove(crs)
            preMap[crs] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0]]
    solution = Solution()
    result = solution.canFinish(numCourses, prerequisites)
    print("Can finish all courses:", result)  
