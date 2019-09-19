def largestRange(array):
    numbers_seen = {}
    largest_range = [array[0], array[0]]

    for num in array:
        numbers_seen[num] = True

    for num in array:
        if num - 1 in numbers_seen:
            continue

        start = num
        end = num

        while num + 1 in numbers_seen:
            num += 1
            end = num

        if (end - start) > (largest_range[1] - largest_range[0]):
            largest_range[0] = start
            largest_range[1] = end

    return largest_range