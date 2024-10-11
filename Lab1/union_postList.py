def union(x, y):
    answer = []
    i, j = 0, 0

    # Loop until both lists are exhausted
    while i < len(x) and j < len(y):
        if x[i] == y[j]:
            # If both elements are the same, add one to the answer and advance both pointers
            answer.append(x[i])
            i += 1
            j += 1
        elif x[i] < y[j]:
            # If x's element is smaller, add it to the answer and advance the x pointer
            answer.append(x[i])
            i += 1
        else:
            # If y's element is smaller, add it to the answer and advance the y pointer
            answer.append(y[j])
            j += 1

    # If there are remaining elements in x, add them to the answer
    while i < len(x):
        answer.append(x[i])
        i += 1

    # If there are remaining elements in y, add them to the answer
    while j < len(y):
        answer.append(y[j])
        j += 1

    return answer

# Example usage:
x = [1, 2, 5, 6, 10]
y = [2, 3, 5, 7, 9, 10]
result = union(x, y)
print(result)  # Output should be [1, 2, 3, 5, 6, 7, 9, 10]