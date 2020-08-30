"""
Palindrome Number 回文数
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        positive_order = [i for i in s]
        print(positive_order)
        reverse_order = [positive_order[i] for i in range(len(positive_order)-1, -1, -1)]
        print(reverse_order)
        if positive_order == reverse_order:
            return True
        else:
            return False

A = Solution()

test_case = 121

print(A.isPalindrome(test_case))

test_case_2 = 987789
test_case_3 = 1234567

print(A.isPalindrome(test_case_2))
print(A.isPalindrome(test_case_3))


