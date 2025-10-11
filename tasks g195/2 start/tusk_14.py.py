def max_subarray_sum(nums):
    if not nums:
        return 0
    ms = 0
    s = 0
    for i in nums:
        s = max(0, s + i)
        ms = max(ms, s)
    return ms
nuns = list(map(int, input().split()))
res = max_subarray_sum(nuns)
print(res)