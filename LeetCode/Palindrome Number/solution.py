class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num = 0
        given_num = x
        if x < 0:
            return False
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        if given_num == reversed_num:
            return True
        else:
            return False
        

solution = Solution()
result = solution.isPalindrome(-121)
print(result)