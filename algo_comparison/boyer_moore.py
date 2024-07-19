def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0:
        return 0
    
    # Preprocessing
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i
    
    # Searching
    s = 0
    while s <= n - m:
        j = m - 1
        
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        if j < 0:
            return s  # Pattern found at position s
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    
    return -1  # Pattern not found
