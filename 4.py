n = 6
dp = [0] * (n)
# Может прыгнуть на +1, +2, +3

# Жоская база
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

# Жоско пробегаемся отталкиваясь от прошлых результатов
for i in range(4, n):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

print(dp[n-1])

