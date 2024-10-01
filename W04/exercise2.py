import multiprocessing
import numpy as np
import time
import psutil

# https://docs.python.org/3/library/multiprocessing.html
# return sum for array
def chunk_sum(numbers):
    return sum(numbers)

def parallel_sum(array, num_chunks):
    chunk_size = len(array) // num_chunks # chunks size = length of array generated
    chunks = [array[i * chunk_size:(i + 1) * chunk_size] for i in range(num_chunks - 1)] # split into even chunks
    chunks.append(array[(num_chunks - 1) * chunk_size:])  # Last chunk includes any remaining elements

    # Create a pool of processes
    with multiprocessing.Pool(processes=num_chunks) as pool:
        chunk_sums = pool.map(chunk_sum, chunks)

    total_sum = sum(chunk_sums)
    return total_sum

def measure_performance(array, num_threads):
    start_time = time.time()

    # Measure system-wide CPU usage before
    cpu_usage_before = psutil.cpu_percent(interval=None)

    # total sum 
    total_sum = parallel_sum(array, num_threads)

    # cpu after
    cpu_usage_after = psutil.cpu_percent(interval=None)
    
    end_time = time.time()

    #get execution time
    execution_time = end_time - start_time
    cpu_usage = cpu_usage_after - cpu_usage_before  

    return total_sum, execution_time, cpu_usage

def find_max_threads():
    large_array = np.random.randint(1, 100, size=100000)
    max_threads = multiprocessing.cpu_count() * 2  

    for num_threads in range(1, max_threads + 1):
        try:
            total, execution_time, cpu_usage = measure_performance(large_array, num_threads)
            print(f"Threads: {num_threads}, Time: {execution_time:.4f}s, CPU Usage: {cpu_usage:.2f}%, Total Sum: {total}")
        except Exception as e:
            print(f"Failed with {num_threads} threads. Error: {e}")
            break

if __name__ == "__main__":
    find_max_threads()