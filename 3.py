from random import randint

n = 10

nums = [randint(-100, 100) for i in range(n)]

def find_longest_subsequence_with_dp(N):
    dp = [1] * len(N)
    max_len = 1
    end_index = 0
    for i in range(1, len(N)):
        if N[i] > N[i-1]:
            dp[i] = dp[i-1] + 1
        if dp[i] > max_len:
            max_len = dp[i]
            end_index = i
            
    print(dp)
    return N[end_index-max_len+1:end_index+1], max_len  

result, max_len = find_longest_subsequence_with_dp(nums)
print('Исходный массив: ',nums)
print('Максимальная возрастающая последовательность: ',result) 
print('Длина: ', max_len) 