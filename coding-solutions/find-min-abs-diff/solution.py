def solve(nums: list) -> int:
    if len(nums) < 2:
        return None   # no pair exists

    nums.sort()
    min_diff = float('inf')

    for i in range(len(nums) - 1):
        diff = abs(nums[i] - nums[i+1])
        if diff < min_diff:
            min_diff = diff

    return min_diff