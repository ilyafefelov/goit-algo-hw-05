def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0:
        return 0
    
    # Preprocessing
    lps = [0] * m
    j = 0
    
    def compute_lps(pattern):
        length = 0
        lps[0] = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
    
    compute_lps(pattern)
    
    # Searching
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j  # Pattern found at position i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1  # Pattern not found