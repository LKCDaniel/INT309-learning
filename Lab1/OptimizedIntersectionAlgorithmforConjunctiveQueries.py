def intersect(list1, list2):
    """Intersect two sorted posting lists and return the sorted result."""
    i, j = 0, 0
    intersection = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            intersection.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return intersection

def optimized_intersect(terms_postings):
    """Perform an optimized intersection of posting lists for multiple terms.

    Args:
    terms_postings (dict): A dictionary where keys are terms and values are the corresponding posting lists.

    Returns:
    list: A list of document IDs that are common across all posting lists of the provided terms.
    """
    # Sort terms by the length of their posting lists (ascending order)
    sorted_terms = sorted(terms_postings, key=lambda term: len(terms_postings[term]))

    # Start with the postings list of the least frequent term
    result = terms_postings[sorted_terms[0]]

    # Intersect with each subsequent term's postings list
    for term in sorted_terms[1:]:
        result = intersect(result, terms_postings[term])
        if not result:  # Early termination if intersection is empty
            break

    return result

# Example usage:
terms_postings = {
    "term1": [1, 2, 3, 5, 6, 10],
    "term2": [2, 3, 5, 10],
    "term3": [3, 5, 7, 8, 10]
}

result = optimized_intersect(terms_postings)
print(result)  # Output should show documents that contain all terms, e.g., [3, 5, 10]