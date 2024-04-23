def cancellation(input_list, stop_word):
    output_list = []
    for element in input_list:
        if element == stop_word:
            break
        output_list.append(element)
    return output_list
def copy_all_but_skip_word(input_list, skip_word):
    output_list = []
    for element in input_list:
        if element != skip_word:
            output_list.append(element)
    return output_list
def my_average(input_list):
    total = sum(input_list)
    count = len(input_list)
    return total / count
# Testing cancellation function
print(cancellation([3, 4, 5, 6, 7, 8], 2))  # Output: [3, 4, 5, 6, 7, 8]
print(cancellation([3, 4, 5, 6, 7, 8], 6))  # Output: [3, 4, 5]

# Testing copy_all_but_skip_word function
print(copy_all_but_skip_word([3, 4, 5, 6, 7, 8, 3, 4, 5], 2))  # Output: [3, 4, 5, 6, 7, 8, 3, 4, 5]
print(copy_all_but_skip_word(["a", "a", "a"], "a"))  # Output: []

# Testing my_average function
print(my_average([84, 61, 99]))  # Output: 81.33333333333333
print(my_average([0.31147488, -0.18365408, 0.27358631, 5]))  # Output: 1.350351775289537
