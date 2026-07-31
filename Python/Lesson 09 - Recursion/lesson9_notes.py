def sum_of_list(list):
    if len(list) == 0:
        return 0

    result = sum_of_list(list[:-1]) + list[-1]

    return result    

print(sum_of_list([1,2,3,4,5]))