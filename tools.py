from collections import defaultdict


def values_frequency(arr):

    count_dict = defaultdict(int)
    for val in arr:
        count_dict[val] += 1

    values = [v[0] for v in count_dict.items()]
    freq = [v[1] for v in count_dict.items()]

    return values, freq


