class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dict = {}

        for i in magazine:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        count = 0

        for i in ransomNote:
            if i in dict:
                if dict[i] > 0:
                    dict[i] -= 1
                    count += 1
                else:
                    return False
            else:
                return False

        if len(ransomNote) == count:
            return True
        else:
            return False