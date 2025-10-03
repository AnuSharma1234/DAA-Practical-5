def print_lcs_dp_table(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    print(" ", end="")
    for ch in Y:
        print(f" {ch}", end="")
    print()
    
    for i in range(m + 1):
        if i == 0:
            print(" ", end="")
        else:
            print(f"{X[i-1]} ", end="")
        for j in range(n + 1):
            print(f"{dp[i][j]:3}", end="")
        print()
    
    return dp

X = "AGCCCTAAGGGCTACCTAGCTT"
Y = "GACAGCCTACAAGCGTTAGCTTG"
dp = print_lcs_dp_table(X, Y)

def print_lcs(dp, X, Y):
    i = len(X)
    j = len(Y)
    lcs = []
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    lcs.reverse()
    return ''.join(lcs)

print(f"The string is :{print_lcs(dp, X, Y)}")
