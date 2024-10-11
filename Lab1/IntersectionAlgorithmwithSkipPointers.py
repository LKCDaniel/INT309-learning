import math

def has_skip(index, length):
    """ Check if a skip is available from the current index. """
    # Assuming skip is available every sqrt(length) elements
    skip_interval = int(math.sqrt(length))
    return (index + skip_interval) < length

def skip(index, list):
    """ Return the index after the skip. """
    skip_interval = int(math.sqrt(len(list)))
    return min(index + skip_interval, len(list) - 1)

def intersect_with_skips(p1, p2):
    answer = []
    i, j = 0, 0
    len_p1, len_p2 = len(p1), len(p2)

    while i < len_p1 and j < len_p2:
        if p1[i] == p2[j]:
            answer.append(p1[i])
            i += 1
            j += 1
        elif p1[i] < p2[j]:
            if has_skip(i, len_p1) and (p1[skip(i, p1)] <= p2[j]):
                i = skip(i, p1)
            else:
                i += 1
        else:
            if has_skip(j, len_p2) and (p2[skip(j, p2)] <= p1[i]):
                j = skip(j, p2)
            else:
                j += 1

    return answer

# Example usage:
p1 = [1, 3, 7, 9, 10, 15, 20, 25, 30]
p2 = [0, 3, 4, 7, 9, 12, 15, 18, 20, 25, 28, 30, 35]
result = intersect_with_skips(p1, p2)
print(result)  # Output should be [3, 7, 9, 15, 20, 25, 30]