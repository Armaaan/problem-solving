def shortest_supersequence(drunk_text, innocuous_text):
    m, n = len(drunk_text), len(innocuous_text)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif drunk_text[i - 1] == innocuous_text[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    
    i, j = m, n
    result = []
    while i > 0 and j > 0:
        if drunk_text[i - 1] == innocuous_text[j - 1]:
            result.append(drunk_text[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] < dp[i][j - 1]:
            result.append(drunk_text[i - 1])
            i -= 1
        else:
            result.append(innocuous_text[j - 1])
            j -= 1
    
    while i > 0:
        result.append(drunk_text[i - 1])
        i -= 1
    while j > 0:
        result.append(innocuous_text[j - 1])
        j -= 1
    
    return ''.join(reversed(result))

drunk_text = input().strip()
innocuous_text = input().strip()
result = shortest_supersequence(drunk_text, innocuous_text)
print(result)