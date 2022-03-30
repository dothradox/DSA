from cProfile import label
import time
from merge_sort import mergeSort
from matplotlib import pyplot as plt
from insertion_sort import insertion_sort

x_insertion = []
y_insertion = []
x_merge = []
y_merge = []
for i in range(1, 1000):
    sorted_list = list(range(1, i))
    start_time = time.time_ns()
    mergeSort(sorted_list)
    end_time = time.time_ns()
    x_merge.append(i)
    y_merge.append(end_time - start_time)

    sample_list = list(range(i, 1, -1))
    start_time = time.time_ns()
    insertion_sort(sample_list)
    end_time = time.time_ns()
    x_insertion.append(i)
    y_insertion.append(end_time - start_time)

plt.plot(x_insertion, y_insertion, label="Insertion Sort Time Complexity")
plt.plot(x_merge, y_merge, label="Merge Sort Time Complexity")
plt.title("Insertion Sort vs Merge Sort Comparison")
plt.xlabel("Number of integers in the list")
plt.ylabel("Time in ns")
plt.legend()
plt.show()
