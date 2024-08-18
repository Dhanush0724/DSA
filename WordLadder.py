from collections import deque

class Solution:

    def wordladderlength(self,startword,targetword,wordList):

        q = deque([(startword,1)])

        wordset = set(wordList)
        wordset.discard(startword)

        while q:
            word,steps = q.popleft()
            
            if word == targetword:
                return steps
            
            for i in range(len(word)):

                original_char = word[i]
                for ch in 'zxcvbnmlkjhgfdsaqwertyuiop':

                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in wordset:
                        wordset.remove(new_word)
                        q.append((new_word, steps + 1))
                word = word[:i] + original_char + word[i+1:]
        
        
        return 0

if __name__ == "__main__":
    wordList = ["des", "der", "dfr", "dgt", "dfs"]
    startWord = "der"
    targetWord = "dfs"

    obj = Solution()
    ans = obj.wordladderlength(startWord, targetWord, wordList)
    print(ans)