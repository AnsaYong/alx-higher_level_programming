#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)

    # Sort dictionary in reverse using value rather than key
    sorted_dict = dict(sorted(a_dictionary.items(),
                       key=lambda item: item[1], reverse=True))

    # Access the highest value from the sorted dictionary
    return (next(iter(sorted_dict)))
