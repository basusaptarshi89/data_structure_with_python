# binary search
# data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
# target = 22
# output = 10 (index of the element in the list) or -1 (if not found)

import logging

logger = logging.getLogger()
logger.setLevel('INFO')

def binary_search(data, target, low, high):

    mid = (low + high) // 2

    print(f"DATA: {data}\nTARGET: {target}\nlow={low}\nhigh={high}\nmid={mid}\n\n")

    if low > high:
        return -1
    elif data[mid] == target:
        return mid
    elif target < data[mid]:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)


data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 23

output = binary_search(data, target, 0, len(data) - 1)
print(output)
