#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_scores = sum(weight * score for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    return (total_scores / total_weight)
