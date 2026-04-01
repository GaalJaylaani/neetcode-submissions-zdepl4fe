class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        best_len = float('inf')
        best_start, best_end = 0, 0
        left = 0

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            while missing == 0:
                if best_len > right - left + 1:
                    best_len = min(best_len, right - left + 1)
                    best_start, best_end = left, right + 1

                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        return s[best_start:best_end] if best_len != float('inf') else ""

