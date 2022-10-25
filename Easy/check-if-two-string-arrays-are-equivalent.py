# slower
# class Solution:
#     def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
#         return ''.join(word1) == ''.join(word2)


# faster
class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        w1, w2 = ''.join(word1), ''.join(word2)

        if len(w1) != len(w2):
            return False

        for i in range(len(w1)):
            if w1[i] != w2[i]:
                return False

        return True