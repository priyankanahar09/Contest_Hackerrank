def max_path_sum(arr):
    n = len(arr)
    dp = [[-1] * 20 for _ in range(n)]
    return recursive(0, 0, arr, n, dp)

def recursive(i, j, arr, n, dp):
    if i < 0 or i >= n or j < 0 or j >= len(arr[i]):
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    down = arr[i][j] + recursive(i + 1, j, arr, n, dp)
    right = arr[i][j] + recursive(i + 1, j + 1, arr, n, dp)

    dp[i][j] = max(down, right)
    return dp[i][j]

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [list(map(int, input().split())) for _ in range(n)]
        result = max_path_sum(arr)
        print(result)
