class Solution:
    def compress(self, chars: list[str]) -> int:
        counter = 0
        total_counter = 0

        for i in range(len(chars)):
            if i==0 or chars[i-1]==chars[i]:
                counter += 1
            else:
                chars[total_counter] = chars[i-1]
                total_counter += 1
                for num in str(counter):
                    if counter == 1:
                        break
                    chars[total_counter] = num
                    total_counter += 1
                counter = 1

        chars[total_counter] = chars[i]
        total_counter += 1
        for num in str(counter):
            if counter == 1:
                break
            chars[total_counter] = num
            total_counter += 1
        
        return total_counter
