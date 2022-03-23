import time
from search import binary_search, linear_search
from matplotlib import pyplot as plt

x = []
y = []
for i in range(1, 100):
    sorted_list = list(range(1, 10000 * i))
    start_time = time.time_ns()
    # binary_search(sorted_list, 0, len(sorted_list) - 1, -1)
    binary_search(
        sorted_list, 0, len(sorted_list) - 1, sorted_list[(len(sorted_list) - 1) // 2]
    )
    # linear_search(sorted_list, sorted_list[0])
    # linear_search(sorted_list, -1)
    end_time = time.time_ns()
    x.append(10000 * i)
    y.append(end_time - start_time)

plt.plot(x, y)
plt.title("Time taken to search an element in a binary search in the worst case")
plt.xlabel("Number of integers in the list")
plt.ylabel("Time in ns")
plt.show()
