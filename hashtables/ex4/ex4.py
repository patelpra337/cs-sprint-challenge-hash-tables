def has_negatives(a):
    """
    YOUR CODE HERE
    """
    nums_dict = {}
    result = []

    for num in a:
        abs_num = abs(num)
        if abs_num in nums_dict:
            value = nums_dict

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
