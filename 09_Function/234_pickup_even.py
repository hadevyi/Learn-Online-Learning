def pickup_even(data):
    result = []
    for detail in data:
        if detail % 2 == 0:
            result.append(detail)
    return result


pickup_even([3, 4, 5, 6, 7, 8])
