class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        left = 0
        max_count = 0

        for right in range(len(s)):

            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1

            my_set.add(s[right])
            max_count = max(max_count, right - left + 1)

        return max_count

        