class Solution:
    def isValid(self, s: str) -> bool:
        heap = []

        charMap = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        
        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in ['{', '[', '(']:
                heap.append(char)
            else:
                if len(heap) == 0:
                    return False
                if char != charMap[heap[-1]]:
                    return False
                else:
                    heap.pop()

        return len(heap) == 0