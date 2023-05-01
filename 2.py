from random import randint

def find(p):
    n = len(p) - 1
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    s = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            dp[i][j] = 10**100
            for k in range(i, j):
                q = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]
                if q < dp[i][j]:
                    dp[i][j] = q
                    s[i][j] = k

    return dp[1][n], s

def print_optimal_parens(s, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j]+1, j)
        print(")", end="")

nums  = [10, 20, 30, 40, 30]
m, s = find(nums)
print("Оптимальное количество операций: ", m)
print_optimal_parens(s, 1, len(nums)-1)




