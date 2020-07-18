def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    my_cache = {}
    result = []

    for i in arrays:
        for j in i:
            if j in my_cache:
                my_cache[j] += 1
            else:
                my_cache[j] = 1
    for newList in my_cache:
        if my_cache[newList] == len(arrays):
            result.append(newList)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
