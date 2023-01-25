def Max (N, K, arr):
    def dp(index, k, even, odd):
        if index == N:
            return 0
        count = 0
        if even == odd and even > 0:
            t_even = arr[index] % 2 == 0
            t_odd = arr[index] % 2 == 1
            count = 1 + dp(index + 1, k - (abs(arr[index] - arr[index - 1])), t_even, t_odd)
        even += arr[index] % 2 == 0
        odd += arr[index] % 2 == 1
        skip = dp(index + 1, k, even, odd)
        return max(count, skip)
    return dp(0, K, 0, 0)
    

N = int(input())
K = int(input())
arr = list(map(int, input().split()))

out_ = Max(N, K, arr)
print (out_)