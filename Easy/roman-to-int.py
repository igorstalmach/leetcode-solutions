class Solution(object):
    def romanToInt(self, s):
        repres = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        
        out = 0
        flag = False
        s = list(s)
        
        for i in range(len(s)):
            if not flag:
                try:
                    if s[i] + s[i+1] in repres:
                        out += repres[s[i] + s[i+1]]
                        flag = True
                    else:
                        out += repres[s[i]]
                except IndexError:
                    out += repres[s[i]]
            else:
                flag = False
                continue
        
        return out