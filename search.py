import time
from matplotlib import pyplot as plt


def linear_search(my_list, target):
    for i, n in enumerate(my_list):
        if n == target:
            print("found")
            return i
    return -1


def binary_search(my_list, left, right, target):
    if right >= left:
        mid = (left + right) // 2
        if my_list[mid] == target:
            return mid
        elif my_list[mid] > target:
            return binary_search(my_list, left, mid - 1, target)
        else:
            return binary_search(my_list, mid + 1, right, target)
    else:
        return -1


x = []
y = []
for i in range(1, 100):
    sorted_list = list(range(1, 10000 * i))

    start_time = time.time_ns()
    binary_search(sorted_list, 0, len(sorted_list) - 1, 0)
    end_time = time.time_ns()

    x.append(10000 * i)
    y.append(end_time - start_time)

plt.plot(x, y)
plt.title("Time taken to search an element in a binary search")
plt.xlabel("Number of integers in the list")
plt.ylabel("Time in ns")
plt.show()
