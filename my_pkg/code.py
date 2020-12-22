def sort(items):

    types = set(type(item) for item in items)
    if len(types) > 1:
        raise ValueError(f"Got multiple types: {types}")

    n = len(items)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items


def foo():
    x = 2
