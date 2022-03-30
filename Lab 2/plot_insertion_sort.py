import time
from insertion_sort import insertion_sort
from matplotlib import pyplot as plt

x = []
y = []
for i in range(1, 1000):
    sample_list = list(range(i, 1, -1))
    # Sample List
    start_time = time.time_ns()
    # Sort function call
    insertion_sort(sample_list)
    end_time = time.time_ns()
    x.append(i)
    y.append(end_time - start_time)

plt.plot(x, y)
plt.title("Insertion Sort sorting time")
plt.xlabel("Number of integers in the list")
plt.ylabel("Time in ns")
plt.show()
