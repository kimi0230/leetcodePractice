# Write a function that takes a string as input and returns the string reversed.

# Example 1:

# Input: "hello"
# Output: "olleh"
# Example 2:

# Input: "A man, a plan, a canal: Panama"
# Output: "amanaP :lanac a ,nalp a ,nam A"

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverseString2(self, s):
        r = list(s)
        i, j = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i] #交換
            i += 1
            j -= 1

        return "".join(r)
        

if __name__ == '__main__':
    sol = Solution()
    input = "amanaP :lanac a ,nalp a ,nam A"
    print(sol.reverseString(input))
    print(sol.reverseString2(input))
