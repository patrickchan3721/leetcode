def longest_palindromic_substring(s: str) -> str:
    if len(s) < 2:
        return s
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    longest_palindrome = ""
    for i in range(len(s)):
        # Check for odd-length palindromes
        palindrome1 = expand_around_center(i, i)
        # Check for even-length palindromes
        palindrome2 = expand_around_center(i, i + 1)
        
        if len(palindrome1) > len(longest_palindrome):
            longest_palindrome = palindrome1
        if len(palindrome2) > len(longest_palindrome):
            longest_palindrome = palindrome2
    
    return longest_palindrome

# Example usage:
s = "babadbabad"
print(longest_palindromic_substring(s))  # Output: "bab" or "aba"

