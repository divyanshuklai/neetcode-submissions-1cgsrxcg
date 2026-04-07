class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters  = {
            '2': ['a', 'b','c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']
        }

        result = []

        self.dfs(digits, letters, 0, "",  result)

        return result

    def dfs(self, digits, letters, index, current, result):
        if index == len(digits):
            if current != "":
                result.append(current)
            return

        for l in letters[digits[index]]:
            current += l
            self.dfs(digits, letters, index+1, current, result)
            current = current[:-1]