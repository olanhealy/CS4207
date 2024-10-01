import multiprocessing
import numpy as np
# https://docs.python.org/3/library/multiprocessing.html


#return sum fir array
def chunk_sum(numbers):
    return sum(numbers)

def parallel_sum(array, num_chunks):
    # Split the array into chunks
    chunk_size = len(array)
    chunks = [array[i * chunk_size:(i + 1) * chunk_size] for i in range(num_chunks)] # split array into chunks each iteration


    # Create a pool of processes
    with multiprocessing.Pool(processes=num_chunks) as pool:
        # Map the chunk_sum function to each chunk
        chunk_sums = pool.map(chunk_sum, chunks)

    # Combine the results from all the chunks
    total_sum = sum(chunk_sums)
    return total_sum

if __name__ == "__main__":
    # Generate a large array of random numbers size to be 10,000
    large_array = np.random.randint(1, 100, size=100000)
    # Get the number of available CPU cores
    num_cores = multiprocessing.cpu_count()

    # Compute the sum in parallel
    total = parallel_sum(large_array, num_cores)
    print(f"Total sum: {total}")
    print(f"Number of cores: {num_cores}")