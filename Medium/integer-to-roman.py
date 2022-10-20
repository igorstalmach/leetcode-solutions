class Solution:
    def intToRoman(self, num: int) -> str:
        units = {
            'a': 'I',
            'b': 'V',
            'c': 'X'
        }

        tens = {
            'a': 'X',
            'b': 'L',
            'c': 'C'
        }

        hundreds = {
            'a': 'C',
            'b': 'D',
            'c': 'M'
        }

        thousands = {
            'a': 'M'
        }

        def convert(num, dict):
            num = int(num)

            if num <= 3:
                return dict['a'] * num

            if num == 4:
                return dict['a'] + dict['b']

            if num <= 8:
                return dict['b'] + dict['a'] * (num % 5)
            
            if num == 9:
                return dict['a'] + dict['c']

        num = str(num)
        order = len(num)

        if order == 1:
            return convert(num[0], units)
        
        if order == 2:
            return convert(num[0], tens) + convert(num[1], units)

        if order == 3:
            return convert(num[0], hundreds) + convert(num[1], tens) + convert(num[2], units)
        
        if order == 4:
            return convert(num[0], thousands) + convert(num[1], hundreds) + convert(num[2], tens) + convert(num[3], units)
