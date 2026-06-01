class Solution:
    def partition(self, s):

        res = []
        sub = []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def generate(i):

            if i == len(s):
                res.append(sub.copy())
                return

            for j in range(i, len(s)):

                if not isPalindrome(i, j):
                    continue

                sub.append(s[i:j+1])

                generate(j + 1)

                sub.pop()

        generate(0)
        return res