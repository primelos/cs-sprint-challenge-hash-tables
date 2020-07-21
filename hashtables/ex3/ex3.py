
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)



def intersection(*args):
    """
    YOUR CODE HERE
    """
    # Your code here
    my_cache = {}
    result = []

    # print(len(arrays))

    for arr in arrays:
        # print('arr', arr)
        for j in arr:
            # print('j',j)
            if j in my_cache:
                my_cache[j] += 1
                if my_cache[j] == len(arrays): # len(arrays) = 3
                    result.append(j)
            else:
                my_cache[j] = 1
    return result

    # for f in arrays:
    #     if 'a' not in f:
    #         continue
    #     if 'b' not in f:
    #         continue
    #     return True
    # return False



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10, 20)) + [1, 2, 3])
    # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 3]
    arrays.append(list(range(5, 15)) + [1, 2, 3])
    # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3]
    arrays.append(list(range(2, 4)) + [1, 2, 3])
    # [2, 3, 1, 2, 3]

    print(intersection(arrays))


print(intersection([[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 3],[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3],[2, 3, 1, 2, 3]]))