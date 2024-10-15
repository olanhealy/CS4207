import multiprocessing


def task_a(number):
    return number * number


def task_b(string):
    return len(string)

def parallel_tasks(numbers, strings):
    # Create a pool of processes
    with multiprocessing.Pool(processes=2) as pool:
        # Map the task_a function to the numbers
        squared_results = pool.map(task_a, numbers)
        # Map the task_b function to the strings
        length_results = pool.map(task_b, strings)

    return squared_results, length_results

if __name__ == "__main__":
    # Example input data
    numbers = [1, 2, 3, 4, 5]
    strings = ["Hello", "World", "Parallel", "Processing"]

    # Execute tasks in parallel
    squared_numbers, string_lengths = parallel_tasks(numbers, strings)

    # Display results
    print(f"Squared Numbers: {squared_numbers}")
    print(f"String Lengths: {string_lengths}")
