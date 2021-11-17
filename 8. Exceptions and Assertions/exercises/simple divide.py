# The ZeroDivisionError exception should not show up when this program is run.

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   # print([simple_divide(item, denom) for item in list_of_numbers])
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0

fancy_divide([0, 2, 4], 0)
# Should return a list with 0 elements
