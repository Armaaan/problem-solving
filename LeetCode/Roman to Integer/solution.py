class Solution:
    def romanToInt(self, s: str) -> int:
        subtracted_value = {
                    "IV": 4,
                    "IX": 9,
                    "XL": 40,
                    "XC": 90,
                    "CD": 400,
                    "CM": 900
                }

        symbols_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        integer_value = 0
        index = 0
        while(index < len(s)):
            if s[index:index+2] in subtracted_value:
                integer_value += subtracted_value[s[index:index+2]]
                index += 2
            else:
                integer_value += symbols_value[s[index]]
                index += 1
        
        return integer_value
    

solution = Solution()
result = solution.romanToInt("III")
print(result)