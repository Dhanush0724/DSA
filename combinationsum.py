class Solution:
    def combinationSum(self, candidates, target):
        result = []
        combination = []

        def findCombination(index, target):
            if target == 0:
                result.append(combination[:])
                return
            if index >= len(candidates):
                return

            # Include the current candidate
            if candidates[index] <= target:
                combination.append(candidates[index])
                findCombination(index, target - candidates[index])
                combination.pop()

            # Exclude the current candidate
            findCombination(index + 1, target)

        findCombination(0, target)
        return result

# Instantiate the Solution class
solution = Solution()

# Define the candidates and the target
candidates = [2, 3, 6, 7]
target = 7

# Get the combinations
ans = solution.combinationSum(candidates, target)

# Print the results
print("Combinations are:")
for comb in ans:
    print(" ".join(map(str, comb)))
