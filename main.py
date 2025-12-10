import random
import timeit
import copy
from functools import partial

# ------------------------------------------------
# MERGE SORT ALGORITHM
# ------------------------------------------------

def merge_sort(list):
    if len(list) <= 1:
        return list
    
    mid = len(list) // 2
    left_half = list[:mid]
    right_half = list[mid:]
    
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# ------------------------------------------------
# INSERTION SORT ALGORITHM
# ------------------------------------------------

def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list

# ------------------------------------------------
# BUILT-IN TIMSORT ALGORITHM
# ------------------------------------------------

def timsort_sort(list):
    return sorted(list) 

# ------------------------------------------------
# TESTS
# ------------------------------------------------

def data_generated_for_tests(size, type = 'random'):
    random_list = [random.randint(0, size) for _ in range(size)]
    if type == 'sorted':
        return sorted(random_list)
    elif type == 'reversed':
        return sorted(random_list, reverse=True)
    return random_list

def run_tests(algorithms, sizes, data_type='random', runs=10):
    results = {name: [] for name in algorithms.keys()}
    
    print(f"\nTests on {data_type} datas...")
    print("-" * 50)
    
    for size in sizes:
        base_data = data_generated_for_tests(size, data_type)
        
        for name, func in algorithms.items():
            if name == "Timsort (sorted)":
                test_func = partial(func, base_data)
            else:
                test_func = partial(func, copy.deepcopy(base_data))

            total_time = timeit.timeit(
                lambda: func(copy.deepcopy(base_data)), 
                number=runs
            )
            avg_time_ms = (total_time / runs) * 1000
            
            results[name].append(avg_time_ms)
            
            print(f"| {name:<20} | Size {size:<8} | Time: {avg_time_ms:.4f} ms |")

    return results

algorithms = {
    "Timsort (sorted)": timsort_sort,
    "Merge Sort": merge_sort,
    "Insertion Sort": insertion_sort,
}

small_sizes = [100, 500, 1000, 2000]
large_sizes = [10000, 50000, 100000]

print("--------------------------- TESTS ----------------------------------")
print("--------------------------------------------------------------------")

results_random = run_tests(algorithms, large_sizes, data_type='random', runs=5)

results_sorted = run_tests(algorithms, large_sizes, data_type='sorted', runs=5)

results_small = run_tests(algorithms, small_sizes, data_type='random', runs=10)

results_small = run_tests(algorithms, large_sizes, data_type='reversed', runs=5)

results_small = run_tests(algorithms, small_sizes, data_type='reversed', runs=5)