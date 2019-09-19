def longestConsecutive(self, nums: List[int]) -> int:
    numbers_seen = {}
    largest_range = 0

    if len(nums) == 0:
        return 0

    for num in nums:
        numbers_seen[num] = True

    for num in nums:
        if num - 1 in numbers_seen:
            continue

        start = num
        end = num

        while num + 1 in numbers_seen:
            num += 1
            end = num

        if end - start > largest_range:
            largest_range = end - start

    return largest_range + 1