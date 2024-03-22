def conditional_return(condition, true_result, false_result):
    if condition:
        return true_result
    return false_result


def all_equal(iterable):
    return len(set(iterable)) == 1
