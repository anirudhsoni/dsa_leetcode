class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        size = len(s)//k
        parts = [s[i:i+size] for i in range(0, len(s)-size+1, size)]
        s_counter = Counter(parts)
        parts_d = [t[i:i+size] for i in range(0, len(t)-size+1, size)]
        t_counter = Counter(parts_d)
        return s_counter == t_counter
        