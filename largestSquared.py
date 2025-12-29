def largestSquared(N, A):
    max_val = max(A)
    min_val = min(A)
    return max(max_val * max_val, min_val * min_val)


if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()

    N = int(data[0])
    A = list(map(int, data[1:1 + N]))  # ensure exactly N elements

    print(largestSquared(N, A))
