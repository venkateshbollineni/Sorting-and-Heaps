import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def write_file(filename, data):
    with open(filename, 'w') as file:
        file.writelines(data)

def sort_and_measure_time(sort_function, data):
    start_time = time.time()
    sorted_data = sort_function(data)
    end_time = time.time()
    return sorted_data, end_time - start_time

def user_selection(prompt, options):
    while True:
        print(prompt)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input("Input your selection(numeric value): ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice) - 1
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    input_type_options = ["Permuted", "Sorted"]
    file_size_options = ["15K", "30K", "45K", "60K", "75K", "90K", "105K", "120K", "135K", "150K"]
    algorithm_options = ["InsertionSort", "MergeSort", "HeapSort"]
    algorithm_abbreviations = ["IS", "MS", "HS"]
    sort_functions = [insertion_sort, merge_sort, heap_sort]

    while True:
        input_type_index = user_selection("Select input file type (1-2):", input_type_options)
        file_size_index = user_selection("\nSelect input file size (1-10):", file_size_options)
        algorithm_index = user_selection("\nSelect sorting algorithm (1-3):", algorithm_options)

        input_type = "perm" if input_type_index == 0 else "sorted"
        file_size = file_size_options[file_size_index]
        algorithm_abbr = algorithm_abbreviations[algorithm_index]
        sort_function = sort_functions[algorithm_index]

        input_file = f"{input_type}{file_size}.txt"
        data = read_file(input_file)
        sorted_data, runtime = sort_and_measure_time(sort_function, data.copy())

        if input_type == "sorted":
            output_file = f"{algorithm_abbr}S{file_size}.txt"
        else:
            output_file = f"{algorithm_abbr}{file_size}.txt"

        write_file(output_file, sorted_data)
        print(f"Sorted {input_file} using {algorithm_abbr}, runtime: {runtime} seconds, output: {output_file}")

        continue_choice = user_selection("Do you want to continue for the next operation?", ["Continue", "Exit"])
        if continue_choice == 1:
            print("Goodbye")
            break
