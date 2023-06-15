#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or not isinstance(my_list, list):
        return 0

    weighted_sum = 0
    total_weight = 0

    for item in my_list:
        if not isinstance(item, tuple) or len(item) != 2 or
        not (isinstance(item[0], int) and isinstance(item[1], int)):
            return 0
        score, weight = item
        weighted_sum += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    return (weighted_sum / total_weight)
